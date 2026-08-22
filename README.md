# iterm-console-usage
MacOs console usage

**iTerm2** is the most visual option on macOS — it's a native app so it gets the most polish.

Key visual features:
- **Split panes** with drag-to-resize
- **Saved window arrangements** — restore your exact layout on launch
- **Built-in tmux integration** (`tmux -CC`) — tmux sessions rendered as native iTerm2 tabs/windows, not raw text
- **Badges** — overlay text on a pane (e.g. show hostname, env, git branch)
- **Status bar** — built-in bottom bar with CPU, memory, current job, git info
- **Broadcast input** — type into multiple panes simultaneously
- **Profile colours** — visually distinguish prod vs dev vs staging sessions at a glance

**Warp** is worth mentioning too — it's a newer terminal built ground-up for UX, with a more "app-like" feel, command blocks, AI assistance, and a very clean visual layout. No configuration needed out of the box.

**Quick pick:**
- Staying classic, want tmux compatibility → **iTerm2**
- Want modern UX with zero setup → **Warp**

Given your Stack Deck + multi-monitor setup, iTerm2's saved arrangements + profile colouring per environment (NESO prod / dev / local homelab) would map well to how you already work.

---

> 🌐 **Live Documentation Portal**: [https://rifaterdemsahin.github.io/iterm-console-usage/](https://rifaterdemsahin.github.io/iterm-console-usage/)

---

## 🛠️ iTerm2 Automation & Watermark Tools

This repository includes CLI and shell tools to inspect running iTerm2 sessions, set watermark badges, lock session headlines, and apply high-contrast color palettes (including classic Matrix Green & Black).

### Quick Commands

```bash
# 1. Switch all active sessions to classic Matrix Green & Black theme:
./scripts/iterm.sh matrix

# 2. List all active windows, panes, watermark badges, and running jobs:
./scripts/iterm.sh list

# 3. Save a markdown inventory snapshot of live sessions:
./scripts/iterm.sh snapshot

# 4. Add or update watermark badge on active pane (or specific session / all sessions):
./scripts/iterm.sh watermark --session current --text "NESO-PROD"

# 5. Apply high-contrast palette with locked headline:
./scripts/iterm.sh style --session current --palette "Matrix" --headline "CLAUDE-MAIN"

# 6. Auto-distribute distinct colors across all open sessions:
./scripts/iterm.sh auto-style --prefix "AGENT"

# 7. Install Dynamic Profiles to macOS iTerm2 configuration:
./scripts/iterm.sh install-profiles
```

### In-Session Shell Escape Helpers (No Python Required)

```bash
source scripts/watermark_helpers.sh
iterm_badge "CLAUDE-A"     # Set badge in current pane
iterm_title "Prod Task"    # Set pane title
iterm_clear_badge          # Clear badge
```

---

## 📚 Documentation Index

### 🖥️ iTerm2 (`docs/iterm2/`)
- [Live Sessions Snapshot (22 Aug 2026)](docs/iterm2/2026-08-22-live-sessions-snapshot.md)
- [How to Use Watermarks & Profiles Guide](docs/iterm2/HOW_TO_USE_WATERMARKS_AND_PROFILES.md)
- [Distinct Color Profiles & Headlines Log](docs/iterm2/2026-08-22-distinct-color-profiles-and-headlines.md)

### ⚡ Warp Guides (`docs/warp/`)
- [Warp AI Features](docs/warp/warp-ai-features.md)
- [Warp Credits Usage](docs/warp/warp-credits-usage.md)
- [Warp xAI & Project Management](docs/warp/warp-xai-and-project-management.md)
- [How Warp Makes Money](docs/warp/HOW_WARP_MAKES_MONEY.md)
- [Git Commit History in Warp](docs/warp/git-commit-history.md)

### ⚖️ Comparisons (`docs/comparisons/`)
- [Why iTerm2 vs Warp with Claude](docs/comparisons/why-iterm-vs-warp-with-claude.md)
