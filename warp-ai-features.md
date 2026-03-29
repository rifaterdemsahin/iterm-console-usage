# Warp Terminal: AI Features Overview

*As of Warp 2.0 (June 2025)*

---

## 1. Natural Language to Command

Type `#` followed by a plain English description and Warp generates the shell command for you. No more searching man pages or Stack Overflow.

```
# list all files larger than 100MB recursively
```

---

## 2. Agent Mode

The flagship AI feature introduced in Warp 2.0. Warp positions itself as an **Agentic Development Environment** — not just a terminal.

| Capability | Description |
|---|---|
| Multi-step automation | Describe a goal; the agent plans and executes multiple commands |
| Context-aware | Reads your environment, tools, and files before acting |
| Interactive app control | Agents operate inside database shells, debuggers, editors, long-running servers |
| Configurable autonomy | Granular permissions: what files it can read, what commands it can run, what it auto-accepts |
| Auto-detection | Warp detects whether you're typing a command or a prompt — or you can lock it to a mode |

---

## 3. AI Autocomplete

Autocomplete powered by shell history + AI context. Suggestions appear inline as you type, reducing typos and speeding up repetitive workflows.

---

## 4. Debug with AI ("Get Help")

When a command exits with an error, Warp adds a **Get Help** button to the failed block. Clicking it sends the command + output to the AI, which:

- Explains what went wrong
- Identifies missing dependencies
- Suggests a fix

---

## 5. Explain Command

Right-click any command or output block → **Ask Warp AI** to get a plain-English explanation of what it does or why it failed.

---

## 6. File & Image Context

Use `@` to attach files or images as context for the AI. Useful when you need the agent to reason about a config file, log, or screenshot.

---

## 7. Warp Drive (Team AI Context)

A centralized knowledge repository that keeps AI context consistent across your team:

- **Reusable workflows** — save and share command notebooks
- **Shared prompts & rules** — coding standards and preferences synced to every agent session
- **Environment variables** — shared across team members
- **Interactive notebooks** — code blocks + documentation, side by side

---

## 8. Multi-Model Support

Warp 2.0 supports multiple LLMs. You can switch mid-session:

- Claude 3.5 Sonnet (default)
- Claude 3 Haiku
- GPT-4o
- Custom models (Enterprise)

---

## 9. Privacy & Data Handling

| Concern | Policy |
|---|---|
| Terminal I/O storage | Never stored on Warp servers |
| Model training | OpenAI and Anthropic are prohibited from using your data |
| Local processing | Natural language detection runs locally; nothing leaves until you press Enter |
| Enterprise | Zero-data retention with LLM providers |

---

## 10. Pricing (AI Requests)

| Plan | AI Requests |
|---|---|
| Free | 100/month |
| Pro/Team | Higher limits |
| Enterprise | Custom + zero retention |

---

## Performance Benchmark

Warp 2.0 ranked **#1 on Terminal-Bench** with a **71% score on SWE-bench Verified** — a standard benchmark for AI coding agents.

---

## Summary

Warp has evolved from a "pretty terminal" into an AI-native coding platform. The core shift with 2.0 is that the AI is not a sidebar chat — it's an agent that runs directly in your terminal, with full access to your shell, files, and running processes, under your control.
