# Warp: xAI Integration & Project Management Report

> Generated: 2026-03-29

---

## 1. Using xAI with Warp

### Overview

xAI (the company behind the Grok models) is one of Warp's contracted LLM backend providers. Warp has a **Zero Data Retention (ZDR)** agreement with xAI, meaning no customer data is retained or used for model training. However, xAI/Grok is **not currently available as a directly user-selectable model** in Warp's model picker.

### Currently Available Models in Warp

| Provider | Models |
|---|---|
| OpenAI | GPT-5, GPT-5.1, GPT-5.1 Codex, GPT-5.2, GPT-5.3 Codex, GPT-5.4 (with varying reasoning levels) |
| Anthropic | Claude Opus 4.5/4.6, Claude Sonnet 4/4.5/4.6, Claude Haiku 4.5 |
| Google | Gemini 2.5 Pro, Gemini 3 Pro |
| z.ai | GLM 4.7 (hosted by Fireworks AI) |
| Auto Modes | Auto (Cost-efficient), Auto (Responsive), Auto (Genius) |

### Bring Your Own Key (BYOK)

Warp supports BYOK on paid plans (Build and above) for **OpenAI, Anthropic, and Google only** — xAI is not currently supported for BYOK.

To configure BYOK: **Settings → AI → API Keys**

### Using xAI/Grok Outside of Warp's Native Picker

1. **Direct API access** — Use the xAI API via `curl` or their SDK from the terminal
2. **Third-party CLI agents** — Integrate a Grok-powered CLI tool using Warp's Third-Party CLI Agents feature

### Data Privacy

Warp is SOC 2 compliant and has Zero Data Retention agreements with all its LLM providers, including xAI. No customer AI data is retained, stored, or used for training.

### Resources

- Model Choice docs: https://docs.warp.dev/agent-platform/capabilities/model-choice
- BYOK docs: https://docs.warp.dev/support-and-community/plans-and-billing/bring-your-own-api-key
- xAI Console: https://console.x.ai
- Feature requests: https://www.warp.dev

---

## 2. Opening Recent Projects in Warp

### Most Recently Accessed Projects

Detected by last-modified time in `~/projects/`:

| # | Project | Last Modified |
|---|---|---|
| 1 | `secondbrain` | Mar 29 (today) |
| 2 | `iterm-console-usage` | Mar 29 (current) |
| 3 | `CAPGEMINI EXPENSES` | Mar 26 |
| 4 | `authentication` | Mar 25 |
| 5 | `dashboard` | Mar 23 |

### Launch Configuration

A Warp Launch Configuration was created at:

```
~/.warp/launch_configurations/recent-projects.yaml
```

This opens all 5 recent projects as colour-coded tabs in a single Warp window.

**To open it:**
1. Press `Cmd+P` to open the Command Palette
2. Type `Launch Configuration`
3. Select **Recent Projects**

### Launch Configuration YAML

```yaml
# Warp Launch Configuration
# Opens the 5 most recently accessed projects as tabs

---
name: Recent Projects
windows:
  - tabs:
      - title: secondbrain
        layout:
          cwd: /Users/rifaterdemsahin/projects/secondbrain
        color: blue
      - title: iterm-console-usage
        layout:
          cwd: /Users/rifaterdemsahin/projects/iterm-console-usage
        color: green
      - title: CAPGEMINI EXPENSES
        layout:
          cwd: /Users/rifaterdemsahin/projects/CAPGEMINI EXPENSES
        color: yellow
      - title: authentication
        layout:
          cwd: /Users/rifaterdemsahin/projects/authentication
        color: magenta
      - title: dashboard
        layout:
          cwd: /Users/rifaterdemsahin/projects/dashboard
        color: cyan
```

---

## 3. Per-Tab Themes in Warp

### Limitation

Warp **does not support per-tab themes**. Themes are a global setting applied to the entire application. There is no `theme:` field in launch configuration YAML files.

### Available Per-Tab Visual Distinction

The only per-tab visual customisation available is the **tab color** (ANSI colors). The launch configuration above already assigns a unique color to each project tab:

| Project | Tab Color |
|---|---|
| secondbrain | Blue |
| iterm-console-usage | Green |
| CAPGEMINI EXPENSES | Yellow |
| authentication | Magenta |
| dashboard | Cyan |

### Changing the Global Theme

Go to **Settings → Appearance → Current Theme** or `Cmd+P` → `Open Theme Picker`.

Built-in themes include: Warp Dark, Warp Light, Dracula, Solarized Dark/Light, Gruvbox Dark/Light, Jellyfish, Koi, Leafy, Marble, Pink City, Snowy, Dark City, Red Rock, Cyber Wave, Willow Dream, Fancy Dracula, Phenomenon, Solar Flare, Adeberry.

Custom themes can be added as `.yaml` files to `~/.warp/themes/` — see the [Warp themes repository](https://github.com/warpdotdev/themes).

---

## Summary

| Topic | Status |
|---|---|
| xAI/Grok selectable in Warp model picker | ❌ Not yet available |
| xAI as backend ZDR provider | ✅ Active |
| BYOK for xAI | ❌ Not supported |
| Recent projects launch config | ✅ Created |
| Per-tab themes | ❌ Not supported (use tab colors instead) |
