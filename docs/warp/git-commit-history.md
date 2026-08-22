# Git Commit History in Warp

## Overview

Warp does not have a built-in git commit history viewer. Use the terminal commands below to browse commit history. Warp's **Code Review panel** handles diffs of uncommitted changes only.

## Commands

### Basic log
```bash
git --no-pager log
```

### Compact one-line view
```bash
git --no-pager log --oneline
```

### Graph view (branches + merges)
```bash
git --no-pager log --oneline --graph --all
```

### With dates and authors
```bash
git --no-pager log --pretty=format:"%h %ad | %s [%an]" --date=short
```

### Filter by author
```bash
git --no-pager log --author="Name"
```

### Filter by date range
```bash
git --no-pager log --after="2024-01-01" --before="2024-12-31"
```

### Show changes in each commit
```bash
git --no-pager log -p
```

### Show stats (files changed, insertions, deletions)
```bash
git --no-pager log --stat
```

### Search commits by keyword in message
```bash
git --no-pager log --grep="keyword"
```

## Warp-Native Git Features

| Feature | How to Access | Purpose |
|---|---|---|
| Code Review panel | `CMD+SHIFT++` | View/edit uncommitted diffs |
| Git diff chip | Bottom input bar | Quick summary of changed files |
| Command History | `CTRL+R` | Search terminal command history |

## Tips

- Always use `--no-pager` in Warp to avoid output being paginated/blocked.
- Pipe to `grep` for quick filtering: `git --no-pager log --oneline | grep "fix"`
- Use `git show <commit-hash>` to inspect a specific commit's changes.
