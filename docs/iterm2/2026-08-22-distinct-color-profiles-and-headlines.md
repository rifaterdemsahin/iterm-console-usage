# iTerm2 distinct colors and headlines — 22 Aug 2026

What was done in this session: inventory live iTerm2 panes, add high-contrast Dynamic Profiles, then paint every live pane with a unique color plus a locked headline/badge so sessions are identifiable at a glance.

## Why

iTerm2 was running many split panes (Claude `agy` and Grok) across three windows. Only two static profiles existed (`Default`, `color`) and both used the same light gray (`fg #101010` / `bg #f9f9f9`). Panes were visually identical. Session titles were also overwritten by the running job (`agy`, `grok`, `ping`).

Goal: assign **distinct contrasting colors** and **stable headlines** so a pane can be picked by color without reading the tab text.

## Inventory at the time of work

iTerm2 process: `/Applications/iTerm.app/Contents/MacOS/iTerm2` (up since Wednesday). Python API was enabled (used for the live restyle).

### Window A — later titled **Grok + Claude**

| Pane (as found) | TTY / job notes |
|---|---|
| Claude (`agy`) | long-running Claude |
| this Grok session | `grok` |
| Claude (`agy`) | long-running Claude |
| Claude (`agy`) | extra shell appeared during restyle |
| Claude (`-zsh`) | extra shell appeared during restyle |

### Window B — later titled **AI Cert + Delivery**

| Pane (as found) | Notable process |
|---|---|
| AI Certification Customer Development (`agy`) | Claude, ~6 days |
| email asistant (`agy`) | Claude |
| Retention and CTR pages… (`grok`) | Grok |
| Delivery Pilot Web (`agy`) | Claude |
| August 2026 GitHub Pages expense dashboard (`grok`) | Grok |
| Claude (`ping`) | `ping -i 1 1.1.1.1` (~1d 21h) |
| Tab 2: GOOGL and RR.L longs… (`grok`) | Grok |

### Window C — later titled **Pexabo + Foundry**

| Pane (as found) | Notable process |
|---|---|
| Codespaces AI agents… (`grok`) | Grok |
| bookmark loader (`agy`) | Claude + Python `http.server 8000` |
| Pexabo Calendar Backup Worker… (`grok`) | Grok + `server.py --port 8775` |
| azure foundry (`agy`) | Claude + Python `http.server 8081` |

Other long-lived system bits seen while listing TTYs (not restyled): WireGuard `wg-quick` for `secondbrain-mac`; `api_server.py` on port 8000 (secondbrain toolbox).

## Files created

### Dynamic Profiles (high-contrast palette)

Path:

```
~/Library/Application Support/iTerm2/DynamicProfiles/contrast-shells.json
```

iTerm2 loads this directory live. Ten named profiles:

| Profile | Background | Foreground | Cursor |
|---|---|---|---|
| Navy White | dark navy | white | gold |
| Crimson White | deep red | white | yellow |
| Forest Lime | dark green | lime | yellow |
| Gold Black | bright gold | black | black |
| Magenta White | magenta | white | gold |
| Cyan Black | cyan | black | black |
| Orange Black | orange | black | black |
| Purple White | purple | white | gold |
| Slate Lime | slate | lime | gold |
| White Navy | near-white | navy | red |

GUIDs are stable (`c0ntrast-…-0001` through `0010`) so iTerm can reload without duplicating profiles.

Existing Dynamic Profile left untouched:

```
~/Library/Application Support/iTerm2/DynamicProfiles/very-light-pink.json
```

That file only tints **Default** background to a very light pink.

### Live restyle (not a file — applied to running sessions)

Named profiles could not be assigned via AppleScript (`Can't set profile name of session`). Full-profile copy via the Python API returned `REQUEST_MALFORMED`. Working method: `iterm2.LocalWriteOnlyProfile` on each session:

- `background_color` / `foreground_color` / `cursor_color` / `bold_color`
- `badge_text` = headline (watermark in the pane)
- `badge_color` with alpha
- `allow_title_setting = False` so `agy`/`grok` cannot steal the headline
- `use_tab_color` + `tab_color` matching the pane
- `session.async_set_name(headline)`
- `window.async_set_title(...)` stored as `titleOverride`

Properties that **failed** (`REQUEST_MALFORMED`) and were skipped: `badge_max_width`, `sync_title`.

Python API used from a throwaway venv: `/tmp/iterm2api` (`pip install iterm2`).

## Final assignment

### Window: **Grok + Claude**

| Headline (badge + tab) | Palette |
|---|---|
| CLAUDE-A | Navy White |
| GROK-THIS | Gold Black |
| CLAUDE-B | Crimson White |
| CLAUDE-C | Slate Lime |
| CLAUDE-D | White Navy |

### Window: **AI Cert + Delivery**

| Headline | Palette |
|---|---|
| AI-CERT | Purple White |
| EMAIL-ASSIST | Orange Black |
| GROK-CTR | Cyan Black |
| DELIVERY-PILOT | Forest Lime |
| GROK-EXPENSE | Magenta White |
| PING-WATCH | Slate Lime |
| GROK-MARKETS (tab 2) | White Navy |

### Window: **Pexabo + Foundry**

| Headline | Palette |
|---|---|
| GROK-CODESPACES | Navy White |
| BOOKMARK-LOADER | Gold Black |
| PEXABO-BACKUP | Crimson White |
| AZURE-FOUNDRY | Forest Lime |

Headlines stay first in the tab. The job name still appends in parentheses (`CLAUDE-A (agy)`). The large badge is the pane watermark.

Palette reuse across *windows* is intentional (10 colors, 16 panes). Headlines are unique globally.

## How to re-apply later

1. Confirm Python API: iTerm2 → Settings → General → Magic → **Enable Python API**.
2. Profiles should already appear under **Profiles** from `contrast-shells.json`.
3. Per pane, either:
   - Session → Change Profile → pick a contrast name, or
   - Re-run a small `iterm2` script that sets `LocalWriteOnlyProfile` colors + `badge_text` + `async_set_name`.
4. To keep headlines from being overwritten: leave `allow_title_setting` off on those sessions.

Manual assign without script: click pane → **Session → Change Profile**.

## What was not done

- Did not rewrite the static `Default` / `color` bookmarks in `com.googlecode.iterm2.plist`.
- Did not save a window arrangement.
- Did not kill leftover jobs (`ping 1.1.1.1`, `http.server`, `server.py --port 8775`).
- Did not persist the `/tmp/iterm2api` venv.
- Color application is **per live session**. New panes still spawn from Default until you pick a profile or re-run the restyle.
