# Warp AI Credits: Where They Are Consumed

> Generated: 2026-03-29

---

## Credit Allowances by Plan

| Plan | AI Requests / Month |
|---|---|
| Free | 100 |
| Pro / Team | Higher limits |
| Enterprise | Custom + zero data retention |

---

## Features That Consume Credits

### 1. Natural Language to Command (`#`)

**Triggered by:** Typing `#` followed by a plain-English description.
**Credit cost:** 1 request per generation.
**Example:**
```
# list all files larger than 100MB recursively
```

---

### 2. Agent Mode

**Triggered by:** Describing a multi-step goal to the Oz agent in the terminal.
**Credit cost:** 1 request per model call — multi-step tasks generate **multiple calls**.
**Notes:** This is the highest credit consumer. A single agentic task may trigger 5–20+ model calls depending on complexity.

---

### 3. AI Autocomplete

**Triggered by:** Typing in the command input; suggestions appear inline.
**Credit cost:** Varies — requests are batched and may be throttled.
**Notes:** Continuous use (long sessions with many keystrokes) can accumulate credits.

---

### 4. Debug with AI ("Get Help")

**Triggered by:** Clicking the **Get Help** button on a failed command block.
**Credit cost:** 1 request per click.
**What it sends:** The failed command + its full output.

---

### 5. Explain Command / Ask Warp AI

**Triggered by:** Right-clicking any command or output block → **Ask Warp AI**.
**Credit cost:** 1 request per explanation.

---

### 6. File & Image Context (`@`)

**Triggered by:** Using `@` to attach files or images as AI context.
**Credit cost:** Included in the agent request it accompanies — but larger context may route to more expensive models.

---

## Model Impact on Credit Weight

Different models consume different amounts of credit budget. Heavier models cost more per request:

| Provider | Models (Current) | Relative Cost |
|---|---|---|
| Anthropic | Claude Opus 4.5 / 4.6 | High |
| Anthropic | Claude Sonnet 4 / 4.5 / 4.6 | Medium |
| Anthropic | Claude Haiku 4.5 | Low |
| OpenAI | GPT-5, GPT-5.1 Codex, GPT-5.2–5.4 | High |
| Google | Gemini 2.5 Pro, Gemini 3 Pro | Medium–High |
| z.ai | GLM 4.7 (via Fireworks AI) | Low–Medium |
| Auto (Cost-efficient) | Warp selects cheapest suitable model | Low |
| Auto (Responsive) | Balanced speed vs cost | Medium |
| Auto (Genius) | Best model for the task | High |

**Tip:** Use **Auto (Cost-efficient)** for simple tasks (command lookup, quick explanations) and reserve higher-tier models for complex agentic workflows.

---

## Bring Your Own Key (BYOK)

Credits from your own API key **do not count against Warp's monthly limit**. BYOK is available on **Build plan and above** for:

- OpenAI
- Anthropic
- Google

> xAI (Grok) is **not currently supported** for BYOK.

To configure: **Settings → AI → API Keys**

---

## Tips to Reduce Credit Usage

| Habit | Impact |
|---|---|
| Use `Auto (Cost-efficient)` model for simple tasks | Low cost per request |
| Batch questions into a single agent prompt | Fewer total requests |
| Use BYOK for heavy workloads | Bypass Warp's monthly limit |
| Avoid clicking "Get Help" repeatedly for the same error | Each click = 1 credit |
| Turn off AI Autocomplete when not needed | Reduces passive credit drain |

---

## Summary

The two largest credit consumers in daily use are **Agent Mode** (multi-call tasks) and **AI Autocomplete** (passive, continuous). Natural Language to Command and Debug with AI are the most predictable: one action = one credit.
