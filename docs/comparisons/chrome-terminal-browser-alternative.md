# 🌐 chromeTerminal: Browser-Native macOS Terminal Alternative

> **Project Repository**: [github.com/rifaterdemsahin/chromeTerminal](https://github.com/rifaterdemsahin/chromeTerminal)  
> **Live Static Guide & Walkthrough**: [rifaterdemsahin.github.io/chromeTerminal](https://rifaterdemsahin.github.io/chromeTerminal/)

---

## 💡 Overview

**`chromeTerminal`** is a browser-based terminal environment for macOS created by Rifat Erdem Sahin as an alternative strategy for managing terminal sessions directly inside **Google Chrome**.

Instead of toggling between native terminal windows (iTerm2, Warp, Terminal.app) and web workflows, `chromeTerminal` embeds a real interactive pseudo-terminal (PTY) into Chrome tabs.

```
+-----------------------------------------------------------------------+
|  Google Chrome Browser (Tabs / Groups / DevTools)                     |
|  http://127.0.0.1:3847                                                |
|  +-----------------------------------------------------------------+  |
|  |  xterm.js Terminal UI (WebSockets)                              |  |
|  +-----------------------------------------------------------------+  |
+-----------------------------------▲-----------------------------------+
                                    │ WebSocket (127.0.0.1:3847)
+-----------------------------------▼-----------------------------------+
|  Local Node.js Server (node-pty)                                      |
|  Spawns real macOS zsh shell locally                                  |
+-----------------------------------------------------------------------+
```

---

## 🎯 Why Use chromeTerminal as a Session Management Tactic?

### 1. Unified Browser Workspace
When paired with cloud dashboards (Azure Portal, Cloudflare, GitHub, Skool) or local web servers, `chromeTerminal` keeps your CLI operations and web tools inside the same browser tab ecosystem:
- **Chrome Tab Groups**: Group related terminals with project web pages (e.g. `[Project-A: App + API + Terminal]`).
- **Tab Pinning & Search**: Pin persistent terminal tabs, search open tabs across windows with `⌘⇧A`.
- **Side-by-Side Split**: Arrange Chrome windows side-by-side with full-screen developer tools.

### 2. Zero Installation Friction
No complex terminal configs or custom desktop builds required. Any device running Chrome on macOS can connect to the local daemon.

### 3. Local PTY Execution & Security Boundary
- Spawns your native macOS shell (`zsh` by default).
- Runs with your exact `~/.zshrc` aliases, scripts, and PATH environment variables.
- Strictly bound to `127.0.0.1:3847` (local loopback) to prevent external exposure.

---

## ⚡ Quick Start

### 1. Clone & Run the Local Server
```bash
git clone https://github.com/rifaterdemsahin/chromeTerminal.git
cd chromeTerminal
npm install
npm start
```

### 2. Open in Google Chrome
```bash
open -a "Google Chrome" http://127.0.0.1:3847
```
Use the **Guide** button in the top menu for the built-in walkthrough.

---

## ⚖️ Comparison: iTerm2 vs Warp vs chromeTerminal

| Capability | iTerm2 | Warp | chromeTerminal |
|---|---|---|---|
| **Runtime Environment** | Native macOS Cocoa / Metal | Rust / GPU accelerated | Google Chrome + Node.js PTY |
| **Session Tracking** | Watermark Badges (`⌘I`) & Titles | Block-based Workflows & Warp Drive | Chrome Tab Groups & Search (`⌘⇧A`) |
| **Customization** | Python API, OSC escape codes, Dynamic Profiles | Built-in themes & AI rules | CSS / Web themes / Chrome extensions |
| **AI Integration** | Claude Code / Grok / AGY CLI integration | Warp AI inline assistant & agent mode | Web AI sidecar tabs / DevTools |
| **Screen Splitting** | Native multi-pane splits & saved arrangements | Native vertical & horizontal splits | Chrome multi-window / tab splitting |
| **Best For** | Heavy terminal multitasking, multi-screen matrix dashboards | Polished AI assistant workflows & block navigation | Browser-centric workflows & web developers |

---

## 🔗 Related Resources & Links

- **Repository**: [https://github.com/rifaterdemsahin/chromeTerminal](https://github.com/rifaterdemsahin/chromeTerminal)
- **Live Static Walkthrough**: [https://rifaterdemsahin.github.io/chromeTerminal/](https://rifaterdemsahin.github.io/chromeTerminal/)
- **iTerm2 Badge Settings Guide**: [../iterm2/iterm2-badge-management-tactic.md](../iterm2/iterm2-badge-management-tactic.md)
- **Why iTerm2 vs Warp with Claude**: [why-iterm-vs-warp-with-claude.md](why-iterm-vs-warp-with-claude.md)
