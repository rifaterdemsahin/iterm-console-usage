# 🏷️ iTerm2 Badge Settings: The Multi-Session Management Tactic

> **Core Tactic**: When running dozens of concurrent terminal panes across multiple monitors, tabs, and windows (e.g., Claude Code instances, Grok watchers, deployment runners, server logs, and production SSH tunnels), standard tab titles are too small and easily obscured. **iTerm2 Badges (Watermarks)** provide an unmissable, semi-transparent background overlay in every pane, giving instant peripheral awareness of each session's role and preventing costly mistakes.

---

## 🎯 Why Use Badges for Multi-Terminal Management?

1. **Zero Eye Fatigue & Instant Orientation**: You don't need to read small 11pt window headers. A glance at the top-right watermark (`CLAUDE-A`, `PROD-DB`, `PING-WATCH`) immediately identifies the session context.
2. **Preventing Production Disasters**: Color-coding + prominent watermarks (`PROD` in red or gold) prevents running destructive commands in the wrong shell.
3. **Session Persistence with AI Agents**: When AI assistants (Claude, AGY, Grok) change process titles dynamically, locked badges stay permanently fixed in the background.
4. **Non-Intrusive**: Badges render *behind* your terminal text with configurable alpha transparency (e.g., 10%–25%), ensuring zero interference with terminal readability.

---

## 🖥️ How to Configure Badges via GUI

### 1. Set Badge on the Active Pane
1. Click into any pane.
2. Open **Session Inspector**: Press `⌘I` (or go to **Session** → **Edit Session...** in the macOS menu).
3. Under the **General** tab:
   - Locate the **Badge** text input field.
   - Type your desired watermark (e.g., `CLAUDE-1`, `DELIVERY-PILOT`, `AZURE-FOUNDRY`).
   - The badge updates in real time in the background.

```
+-------------------------------------------------------------+
| Session Settings (⌘I)                                       |
| [General] [Colors] [Text] [Window] [Terminal] [Keys]        |
+-------------------------------------------------------------+
| Name:       CLAUDE-A                                        |
| Badge:      [ CLAUDE-A                                   ]  | <--- Set here
| ...                                                         |
+-------------------------------------------------------------+
```

### 2. Adjust Badge Color & Transparency (Alpha)
1. Go to **Settings (⌘,)** → **Profiles** → **Colors** tab (or `⌘I` → **Colors** for session-only).
2. Look for the **Badge** color box on the right color palette.
3. Click the color chip to open the macOS Color Picker.
4. Adjust the **Opacity Slider (Alpha)**:
   - **Recommended for Dark/Matrix Themes**: `12% – 20%` white or bright neon green.
   - **Recommended for High-Contrast Themes**: `15% – 25%` opacity.

---

## ⚡ Dynamic Badge Formulas & Interpolation

iTerm2 supports dynamic variable interpolation inside the Badge field! You can enter dynamic strings to automatically display live status:

| Badge String | Description |
|---|---|
| `\(session.name)` | Displays the current session title |
| `\(session.jobName)` | Displays the currently running foreground command (e.g. `node`, `python`, `git`) |
| `\(session.path)` | Shows the current working directory path |
| `\(session.username)@\(session.hostname)` | Shows the SSH user and server name |
| `\(user.gitBranch)` | Displays the current Git branch (if shell integration is enabled) |
| `\(session.badge) | \(session.jobName)` | Combines static watermark badge with active process name |

---

## 🚀 Programmatic Badge Control (CLI & Automation)

### Method 1: Using the Project's CLI Manager
This repository includes a Python API manager to inspect and set badges across live sessions:

```bash
# Set watermark on the active pane
./scripts/iterm.sh watermark --session current --text "CLAUDE-A"

# Set watermark with custom alpha opacity (e.g., 20%)
./scripts/iterm.sh watermark --session current --text "PROD-SERVER" --alpha 0.20

# Target a specific pane by session ID or search term
./scripts/iterm.sh watermark --session "28A4215F" --text "AI-CERT"

# Broadcast a watermark to ALL open panes simultaneously
./scripts/iterm.sh watermark --session all --text "GLOBAL-TEST"
```

### Method 2: Shell OSC Escape Sequence (Zero Dependencies)
You can change the watermark badge on the fly from any bash/zsh prompt or shell script using standard ANSI OSC escape code `1337`:

```bash
# In-terminal command to set badge:
printf "\e]1337;SetBadgeFormat=%s\a" $(echo -n "CLAUDE-MAIN" | base64)

# In-terminal command to clear badge:
printf "\e]1337;SetBadgeFormat=\a"
```

### Method 3: Shell Functions (`scripts/watermark_helpers.sh`)
Source the helper script in your `~/.zshrc`:
```bash
source scripts/watermark_helpers.sh

# Simple aliases
iterm_badge "STAGE-ENV"
iterm_clear_badge
```

---

## 📋 Recommended Badge Naming Conventions

For optimal clarity across multi-screen setups, structure badge names by function and role:

| Category | Example Badges | Recommended Color Palette |
|---|---|---|
| **AI Assistants** | `CLAUDE-A`, `CLAUDE-B`, `GROK-CTR`, `AGY-DEV` | Navy White / Matrix Green |
| **Cloud & Deployments** | `AZURE-FOUNDRY`, `AWS-PROD`, `K8S-CLUSTER` | Forest Lime / Crimson White |
| **Background Monitors** | `PING-WATCH`, `DOCKER-LOGS`, `HEALTH-CHECK` | Slate Lime |
| **Feature Workspaces** | `PEXABO-BACKUP`, `BOOKMARK-LOADER`, `DELIVERY-PILOT` | Gold Black / Cyan Black |
| **Communications** | `EMAIL-ASSIST`, `SLACK-BOT`, `NOTIFICATIONS` | Orange Black |

---

## 🔗 Related Resources

- [How to Use Watermarks & Profiles Guide](HOW_TO_USE_WATERMARKS_AND_PROFILES.md)
- [Live Sessions Snapshot](2026-08-22-live-sessions-snapshot.md)
- [Distinct Color Profiles & Headlines Log](2026-08-22-distinct-color-profiles-and-headlines.md)
- [Dynamic Profile Definitions (contrast-shells.json)](../../profiles/contrast-shells.json)
- [iTerm2 Official Badge Documentation](https://iterm2.com/documentation-badges.html)
