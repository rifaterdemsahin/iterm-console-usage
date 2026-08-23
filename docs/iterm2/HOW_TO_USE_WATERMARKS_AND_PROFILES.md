# iTerm2 Session Management, Watermarks & Dynamic Profiles Guide

This guide explains how to reach live iTerm2 sessions, inspect running processes, apply high-contrast color palettes, lock headlines, and trigger watermark badges.

---

## 🚀 Quick Start

Ensure iTerm2's Python API is enabled:
> **iTerm2** → **Settings (⌘,)** → **General** → **Magic** → check **Enable Python API**

### 1. List All Active Windows, Panes & Processes
Reach into iTerm2 and inspect every active session, window, tab, watermark badge, and running process:
```bash
./scripts/iterm.sh list
```

### 2. Set Watermarks (Badges)
Add or update the background watermark badge text in any pane:

- **Active / Current session:**
  ```bash
  ./scripts/iterm.sh watermark --session current --text "NESO-PROD"
  ```
- **Specific session by name or ID:**
  ```bash
  ./scripts/iterm.sh watermark --session "CLAUDE-A" --text "CRITICAL"
  ./scripts/iterm.sh watermark --session "28A4215F" --text "AI-DEV"
  ```
- **All open sessions at once:**
  ```bash
  ./scripts/iterm.sh watermark --session all --text "MAINTENANCE"
  ```
- **Custom badge opacity (alpha):**
  ```bash
  ./scripts/iterm.sh watermark --session current --text "HOMELAB" --alpha 0.35
  ```

### 3. Apply High-Contrast Palette & Locked Headline
Apply one of the 10 contrast palettes, set the tab color to match, apply the watermark badge, and lock the headline so foreground jobs cannot steal the title:
```bash
./scripts/iterm.sh style --session current --palette "Navy White" --headline "CLAUDE-MAIN"
```

Available palettes:
- `Navy White` (dark navy / white text / gold cursor)
- `Crimson White` (deep red / white text / yellow cursor)
- `Forest Lime` (dark green / lime text / yellow cursor)
- `Gold Black` (bright gold / black text / black cursor)
- `Magenta White` (magenta / white text / gold cursor)
- `Cyan Black` (cyan / black text / black cursor)
- `Orange Black` (orange / black text / black cursor)
- `Purple White` (purple / white text / gold cursor)
- `Slate Lime` (slate / lime text / gold cursor)
- `White Navy` (near-white / navy text / red cursor)

### 4. Auto-Distribute Distinct Colors Across All Sessions
Automatically assign rotating distinct contrast palettes and locked headlines to all open sessions in one click:
```bash
./scripts/iterm.sh auto-style --prefix "AGENT"
```

### 5. Install / Sync Dynamic Profiles
Install the dynamic profiles JSON so all 10 profiles are available in iTerm2's native **Profiles** menu:
```bash
./scripts/iterm.sh install-profiles
```
*(Installs to `~/Library/Application Support/iTerm2/DynamicProfiles/contrast-shells.json`)*

---

## ⚡ Instant In-Session Shell Helpers (No Python Required)

Source the helper functions in your current shell or add them to your `~/.zshrc`:
```bash
source scripts/watermark_helpers.sh
```

Then trigger watermarks directly from command-line using native OSC escape sequences:

```bash
# Set watermark badge
iterm_badge "CLAUDE-DEV"

# Clear watermark badge
iterm_clear_badge

# Set window / tab title
iterm_title "NESO / Prod Deployment"

# Set tab color (RGB values 0 to 255)
iterm_tab_color 255 120 0

# Set terminal background color (Hex)
iterm_bg_color "#0d1b2a"
```

---

## 🔧 Manual GUI Fix (Session Settings)

If a session's background color is stuck (e.g. from an old profile or setting) or you want to manually adjust colors/badges directly in the iTerm2 GUI without running commands:

1. Click into the target pane/session.
2. From the top macOS menu bar, go to: **Session** → **Edit Session...** (or press `⌘I`).
3. Navigate to **General** (or **Colors**) to directly customize:
   - Profile settings & defaults
   - Background and Foreground colors
   - Badge text & alpha watermark opacity
4. Alternatively, quickly swap the palette via **Session** → **Change Profile** and select any profile (e.g., *Matrix*, *Readable Pro*, *Navy White*).

---

## 🛠️ Architecture & Files

- **`scripts/iterm.sh`**: Zero-dependency bash runner that auto-configures a Python virtual environment and invokes the manager CLI.
- **`scripts/iterm2_manager.py`**: Python API tool implementing session inspection, badge setting, locked headlines, and palette styling.
- **`scripts/watermark_helpers.sh`**: ANSI OSC escape sequence functions for instant in-terminal control.
- **`profiles/contrast-shells.json`**: Dynamic Profile definitions with 10 high-contrast themes.
- **`profiles/default-matrix.json`**: Dynamic Profile setting Default profile to Matrix theme.
- **`docs/iterm2/2026-08-22-distinct-color-profiles-and-headlines.md`**: Initial design inventory and rationale.
