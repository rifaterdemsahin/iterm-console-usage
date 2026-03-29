# Why Use iTerm2 or Warp with Claude Code

## The Core Question

Claude Code runs in your terminal. The terminal you choose directly affects how smoothly you can work — how readable output is, how quickly you can navigate between contexts, and how well the tool integrates with the rest of your workflow.

---

## iTerm2 with Claude Code

### Rationale

iTerm2 gives you fine-grained control over your environment, which matters when Claude Code is running long tasks or managing multiple workstreams.

**Split panes** — run Claude Code in one pane, watch a running server or test output in another. No alt-tabbing.

**Saved window arrangements** — open your exact layout (Claude session, editor, logs, git status) with one command. Consistent context every time.

**Profile colours per environment** — colour-code prod vs dev vs local sessions. When Claude is executing commands, you always know which environment you're in at a glance.

**tmux integration (`tmux -CC`)** — Claude Code sessions can persist across disconnects. If you're running a long agentic task and your terminal drops, the session keeps going. iTerm2 renders tmux natively as tabs/windows rather than raw escape codes.

**Broadcast input** — send the same command to multiple panes simultaneously. Useful when coordinating Claude across multiple project directories.

**Status bar** — see CPU/memory while Claude is doing heavy lifting (building, testing, file operations), so you know when to wait vs intervene.

### Best for
- Users who want full control and already have a configured workflow
- Multi-environment setups (prod / staging / dev / homelab)
- Long-running agentic tasks where session persistence matters
- tmux users who want native rendering

---

## Warp with Claude Code

### Rationale

Warp is built ground-up as a modern terminal with UX as a first-class concern. It removes friction — especially for users new to terminal-heavy workflows.

**Command blocks** — each command and its output is a discrete, selectable block. When Claude Code produces long output, you can scroll and reference specific command results cleanly rather than hunting through a scrollback buffer.

**Built-in AI assistance** — Warp has its own AI features that complement (not replace) Claude Code. You get two layers: Warp for shell command suggestions, Claude Code for code generation and agentic tasks.

**Zero configuration** — works well out of the box. No `.zshrc` tuning or profile setup needed to get a clean, readable experience.

**Modern rendering** — text output from Claude Code (diffs, file trees, task progress) renders clearly with good contrast and spacing by default.

**Collaborative features** — Warp Drive lets you share terminal sessions and command outputs, useful for reviewing what Claude did with a teammate.

### Best for
- Users who want minimal setup and a clean default experience
- Teams that review Claude's work together
- Workflows where command output readability is the top priority
- Users who prefer a GUI-forward, app-like terminal feel

---

## Side-by-Side Summary

| Factor | iTerm2 | Warp |
|---|---|---|
| Setup effort | High (worth it) | Near zero |
| Session persistence | Excellent (tmux -CC) | Good |
| Multi-environment clarity | Profile colours, badges | Visual blocks |
| Long output readability | Scrollback + search | Command blocks (cleaner) |
| AI integration | Claude Code only | Claude Code + Warp AI |
| Team collaboration | Limited | Built-in (Warp Drive) |
| Configuration control | Full | Limited |
| tmux compatibility | Native rendering | Standard |

---

## Recommendation

**Use iTerm2** if you are managing multiple environments, rely on tmux for session persistence, or have an existing terminal configuration you want to preserve. It maps well to complex, multi-context Claude Code workflows.

**Use Warp** if you want the fastest path to a productive Claude Code setup, prefer readable command output blocks, or work in a team context where sharing terminal sessions has value.

Both are solid. The choice is about your existing workflow, not capability.
