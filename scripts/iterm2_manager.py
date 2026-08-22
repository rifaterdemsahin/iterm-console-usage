#!/usr/bin/env python3
"""
iTerm2 Session & Watermark Manager
Manage running iTerm2 sessions, inspect windows/tabs/panes, apply high-contrast
color profiles, and set locked headlines / watermark badges.
"""

import sys
import os
import shutil
import argparse
import asyncio
import json
from pathlib import Path

try:
    import iterm2
except ImportError:
    print("Error: 'iterm2' Python module is not installed.", file=sys.stderr)
    print("Run via './scripts/iterm.sh' to auto-bootstrap the environment, or run: pip install iterm2", file=sys.stderr)
    sys.exit(1)

# Color palettes (matching dynamic profiles)
PALETTES = {
    "Navy White": {
        "fg": (0.95, 0.97, 1.0),
        "bg": (0.05, 0.12, 0.28),
        "cursor": (1.0, 0.84, 0.0),
        "badge_color": (1.0, 1.0, 1.0, 0.2),
        "badge_default": "NAVY"
    },
    "Crimson White": {
        "fg": (1.0, 0.97, 0.94),
        "bg": (0.45, 0.05, 0.08),
        "cursor": (1.0, 0.92, 0.4),
        "badge_color": (1.0, 1.0, 1.0, 0.2),
        "badge_default": "CRIMSON"
    },
    "Forest Lime": {
        "fg": (0.75, 1.0, 0.55),
        "bg": (0.04, 0.18, 0.08),
        "cursor": (1.0, 1.0, 0.3),
        "badge_color": (0.75, 1.0, 0.55, 0.2),
        "badge_default": "FOREST"
    },
    "Gold Black": {
        "fg": (0.12, 0.09, 0.0),
        "bg": (0.95, 0.75, 0.08),
        "cursor": (0.0, 0.0, 0.0),
        "badge_color": (0.0, 0.0, 0.0, 0.2),
        "badge_default": "GOLD"
    },
    "Magenta White": {
        "fg": (1.0, 0.95, 1.0),
        "bg": (0.42, 0.0, 0.42),
        "cursor": (1.0, 0.85, 0.2),
        "badge_color": (1.0, 1.0, 1.0, 0.2),
        "badge_default": "MAGENTA"
    },
    "Cyan Black": {
        "fg": (0.02, 0.08, 0.12),
        "bg": (0.0, 0.78, 0.85),
        "cursor": (0.0, 0.0, 0.0),
        "badge_color": (0.0, 0.0, 0.0, 0.2),
        "badge_default": "CYAN"
    },
    "Orange Black": {
        "fg": (0.08, 0.04, 0.0),
        "bg": (0.95, 0.42, 0.05),
        "cursor": (0.0, 0.0, 0.0),
        "badge_color": (0.0, 0.0, 0.0, 0.2),
        "badge_default": "ORANGE"
    },
    "Purple White": {
        "fg": (0.96, 0.94, 1.0),
        "bg": (0.22, 0.08, 0.48),
        "cursor": (1.0, 0.85, 0.2),
        "badge_color": (1.0, 1.0, 1.0, 0.2),
        "badge_default": "PURPLE"
    },
    "Slate Lime": {
        "fg": (0.72, 1.0, 0.2),
        "bg": (0.12, 0.14, 0.18),
        "cursor": (1.0, 0.9, 0.2),
        "badge_color": (0.72, 1.0, 0.2, 0.2),
        "badge_default": "SLATE"
    },
    "White Navy": {
        "fg": (0.05, 0.12, 0.28),
        "bg": (0.96, 0.97, 1.0),
        "cursor": (0.85, 0.15, 0.1),
        "badge_color": (0.05, 0.12, 0.28, 0.2),
        "badge_default": "LIGHT"
    }
}

PALETTE_KEYS = list(PALETTES.keys())


def make_color(r: float, g: float, b: float, a: float = 1.0) -> iterm2.Color:
    return iterm2.Color(int(r * 255), int(g * 255), int(b * 255), int(a * 255))


async def get_all_sessions(app):
    """Return a flat list of (window, tab, session) tuples."""
    results = []
    for window in app.terminal_windows:
        for tab in window.tabs:
            for session in tab.sessions:
                results.append((window, tab, session))
    return results


async def find_session_by_identifier(app, identifier: str):
    """Find a session by ID, title, or 'current'/'active'."""
    all_sessions = await get_all_sessions(app)
    if not all_sessions:
        return None, None, None

    if identifier in ("current", "active", "focused"):
        curr_win = app.current_terminal_window
        if curr_win and curr_win.current_tab:
            curr_sess = curr_win.current_tab.current_session
            if curr_sess:
                return curr_win, curr_win.current_tab, curr_sess

    # Match by exact session ID
    for w, t, s in all_sessions:
        if s.session_id == identifier:
            return w, t, s

    # Match by partial session ID
    for w, t, s in all_sessions:
        if identifier in s.session_id:
            return w, t, s

    # Match by session name
    for w, t, s in all_sessions:
        name = await s.async_get_variable("session.name") or ""
        badge = await s.async_get_variable("session.badge") or ""
        if identifier.lower() in name.lower() or identifier.lower() in badge.lower():
            return w, t, s

    return None, None, None


async def cmd_list(connection):
    app = await iterm2.async_get_app(connection)
    print("=" * 80)
    print(f"{'WINDOW / TAB':<25} | {'SESSION ID':<22} | {'BADGE / WATERMARK':<18} | {'NAME / TITLE'}")
    print("-" * 80)

    win_count = 0
    total_panes = 0

    for win_idx, window in enumerate(app.terminal_windows, 1):
        win_count += 1
        win_title = await window.async_get_variable("window.titleOverride") or f"Window {win_idx}"
        print(f"\n🖥️  Window {win_idx}: {win_title} (ID: {window.window_id})")

        for tab_idx, tab in enumerate(window.tabs, 1):
            for sess_idx, session in enumerate(tab.sessions, 1):
                total_panes += 1
                name = await session.async_get_variable("session.name") or "(unnamed)"
                badge = await session.async_get_variable("session.badge") or "-"
                job = await session.async_get_variable("session.jobName") or ""
                tty = await session.async_get_variable("session.tty") or ""

                loc = f"  Tab {tab_idx} (Pane {sess_idx})"
                extra = f"{name}"
                if job:
                    extra += f" [{job}]"
                if tty:
                    extra += f" ({tty})"

                print(f"{loc:<25} | {session.session_id:<22} | {badge:<18} | {extra}")

    print("\n" + "=" * 80)
    print(f"Total: {win_count} windows, {total_panes} active panes/sessions.")


async def apply_style_to_session(session, palette_name: str, headline: str = None, lock_title: bool = True):
    if palette_name not in PALETTES:
        raise ValueError(f"Unknown palette '{palette_name}'. Available: {list(PALETTES.keys())}")

    p = PALETTES[palette_name]
    profile = iterm2.LocalWriteOnlyProfile()

    # Colors
    profile.set_foreground_color(make_color(*p["fg"]))
    profile.set_background_color(make_color(*p["bg"]))
    profile.set_cursor_color(make_color(*p["cursor"]))
    profile.set_bold_color(make_color(*p["fg"]))

    # Tab color
    profile.set_use_tab_color(True)
    profile.set_tab_color(make_color(*p["bg"]))

    # Watermark Badge
    badge_text = headline if headline else p["badge_default"]
    profile.set_badge_text(badge_text)
    profile.set_badge_color(make_color(*p["badge_color"]))

    # Title locking
    if lock_title:
        profile.set_allow_title_setting(False)

    await session.async_set_profile_properties(profile)

    if headline:
        await session.async_set_name(headline)


async def cmd_watermark(connection, args):
    app = await iterm2.async_get_app(connection)
    
    if args.session.lower() == "all":
        all_sessions = await get_all_sessions(app)
        for _, _, session in all_sessions:
            profile = iterm2.LocalWriteOnlyProfile()
            profile.set_badge_text(args.text)
            if args.alpha is not None:
                profile.set_badge_color(make_color(1.0, 1.0, 1.0, float(args.alpha)))
            await session.async_set_profile_properties(profile)
        print(f"✅ Set watermark badge '{args.text}' on all {len(all_sessions)} sessions.")
        return

    _, _, session = await find_session_by_identifier(app, args.session)
    if not session:
        print(f"❌ Session '{args.session}' not found. Use 'list' command to see available sessions.", file=sys.stderr)
        sys.exit(1)

    profile = iterm2.LocalWriteOnlyProfile()
    profile.set_badge_text(args.text)
    if args.alpha is not None:
        profile.set_badge_color(make_color(1.0, 1.0, 1.0, float(args.alpha)))
    
    await session.async_set_profile_properties(profile)
    print(f"✅ Set watermark badge '{args.text}' on session {session.session_id}.")


async def cmd_style(connection, args):
    app = await iterm2.async_get_app(connection)
    
    _, _, session = await find_session_by_identifier(app, args.session)
    if not session:
        print(f"❌ Session '{args.session}' not found. Use 'list' command to see available sessions.", file=sys.stderr)
        sys.exit(1)

    palette = args.palette
    # Fuzzy match palette name
    matched_palette = None
    for k in PALETTES:
        if palette.lower() in k.lower():
            matched_palette = k
            break

    if not matched_palette:
        print(f"❌ Palette '{palette}' not recognized. Available: {list(PALETTES.keys())}", file=sys.stderr)
        sys.exit(1)

    await apply_style_to_session(
        session=session,
        palette_name=matched_palette,
        headline=args.headline,
        lock_title=not args.unlock_title
    )
    print(f"✅ Applied palette '{matched_palette}' with badge/headline '{args.headline or matched_palette}' to session {session.session_id}.")


async def cmd_auto_distribute(connection, args):
    """Automatically assign rotating distinct contrast palettes and headlines across all sessions."""
    app = await iterm2.async_get_app(connection)
    all_sessions = await get_all_sessions(app)
    
    if not all_sessions:
        print("No active iTerm2 sessions found.")
        return

    print(f"🎨 Distributing {len(PALETTE_KEYS)} high-contrast palettes across {len(all_sessions)} active sessions...")

    for i, (win, tab, session) in enumerate(all_sessions):
        palette_name = PALETTE_KEYS[i % len(PALETTE_KEYS)]
        current_name = await session.async_get_variable("session.name") or f"PANE-{i+1}"
        headline = args.prefix + f"-{i+1}" if args.prefix else current_name

        await apply_style_to_session(
            session=session,
            palette_name=palette_name,
            headline=headline,
            lock_title=True
        )
        print(f"  • Session {session.session_id} -> {palette_name} ({headline})")

    print(f"✅ Finished styling {len(all_sessions)} sessions with distinct colors and locked headlines.")


def cmd_install_profiles():
    """Install contrast-shells.json into ~/Library/Application Support/iTerm2/DynamicProfiles/"""
    src = Path(__file__).resolve().parent.parent / "profiles" / "contrast-shells.json"
    dest_dir = Path.home() / "Library" / "Application Support" / "iTerm2" / "DynamicProfiles"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / "contrast-shells.json"

    if not src.exists():
        print(f"❌ Source profile file not found at: {src}", file=sys.stderr)
        sys.exit(1)

    shutil.copy2(src, dest)
    print(f"✅ Installed Dynamic Profiles to:\n   {dest}")
    print("iTerm2 loads dynamic profiles automatically in real-time.")


def main():
    parser = argparse.ArgumentParser(
        description="iTerm2 Session & Watermark Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ./scripts/iterm.sh list
  ./scripts/iterm.sh watermark --session current --text "PROD-SERVER"
  ./scripts/iterm.sh style --session current --palette "Navy White" --headline "CLAUDE-A"
  ./scripts/iterm.sh auto-style --prefix "DEV"
  ./scripts/iterm.sh install-profiles
        """
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list
    subparsers.add_parser("list", help="List all open iTerm2 windows, tabs, sessions, badges, and processes")

    # watermark
    p_wm = subparsers.add_parser("watermark", help="Set watermark badge text on a session")
    p_wm.add_argument("--session", default="current", help="Session ID, name, 'current', or 'all' (default: current)")
    p_wm.add_argument("--text", required=True, help="Watermark badge text")
    p_wm.add_argument("--alpha", type=float, default=None, help="Badge opacity alpha (0.0 to 1.0, e.g. 0.25)")

    # style
    p_style = subparsers.add_parser("style", help="Apply a high-contrast color palette and headline to a session")
    p_style.add_argument("--session", default="current", help="Session ID, name, or 'current' (default: current)")
    p_style.add_argument("--palette", required=True, choices=list(PALETTES.keys()) + [k.lower() for k in PALETTES.keys()], help="Palette name")
    p_style.add_argument("--headline", default=None, help="Headline for session name and watermark badge")
    p_style.add_argument("--unlock-title", action="store_true", help="Allow running programs to overwrite session title")

    # auto-style
    p_auto = subparsers.add_parser("auto-style", help="Distribute rotating distinct contrast palettes and headlines across all sessions")
    p_auto.add_argument("--prefix", default=None, help="Optional headline prefix (e.g. WORK, AGENT, PANE)")

    # install-profiles
    subparsers.add_parser("install-profiles", help="Install contrast-shells.json into iTerm2 DynamicProfiles directory")

    args = parser.parse_args()

    if args.command == "install-profiles":
        cmd_install_profiles()
        return

    async def async_main(connection):
        if args.command == "list":
            await cmd_list(connection)
        elif args.command == "watermark":
            await cmd_watermark(connection, args)
        elif args.command == "style":
            await cmd_style(connection, args)
        elif args.command == "auto-style":
            await cmd_auto_distribute(connection, args)

    try:
        iterm2.run_until_complete(async_main)
    except Exception as e:
        print(f"Error connecting to iTerm2: {e}", file=sys.stderr)
        print("Make sure iTerm2 is running and Python API is enabled:", file=sys.stderr)
        print("  iTerm2 -> Settings -> General -> Magic -> Enable Python API", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
