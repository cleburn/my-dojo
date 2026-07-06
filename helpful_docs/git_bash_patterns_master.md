# Git & Bash Patterns Master Reference
## Systematic Command Line Fluency Curriculum

**Created:** December 13, 2025  
**Last Updated:** January 3, 2026

**Integration Status:** Active — supplemental curriculum for weekends and Type B days. Not part of daily Foundation Drilling. 

---

## Integration with Daily Workflow

### Integration Approach

**Decision:** Supplemental curriculum — not part of mandatory daily Foundation Drilling.

**When to use:**
- Type B days (recovery): Pick 1-2 commands for light practice
- Weekends: Dedicated 15-30 min command line drill session
- As-needed: When a project requires unfamiliar Git/Bash operations

**Why not daily:** Python fluency is the bottleneck for AI Engineering. Command line skills compound more slowly and are easier to look up. Prioritize Python patterns in Foundation Drilling; use this doc for enrichment.

### Teaching Format Template

When introducing any new pattern, use this format:

```bash
# Basic pattern
<command template>

# Real example
<concrete command with actual values>
# Translation: "<plain English explanation>"

# Common variations
<2-3 variations showing flexibility>
```

### Repetition Rules

| Pattern Value | Repetition | Advancement Criteria |
|---------------|------------|----------------------|
| High | 3-4 sessions drilling | Can execute without looking up flags |
| Medium | 2-3 sessions drilling | Can recognize and apply with minor reference |
| Lower | Single exposure | Saved in notes, can look up when needed |

---

## Git Pattern Catalog

### HIGH PRIORITY — Daily Professional Use

These patterns appear constantly in professional workflows. Must reach "Adopted" status.

---

#### Category: Core Workflow

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `git status` | Check working directory state | 1 | Adopted |
| `git add .` | Stage all changes | 1 | Adopted |
| `git commit -m` | Commit with message | 1 | Adopted |
| `git push` | Push to remote | 1 | Adopted |
| `git pull` | Fetch and merge from remote | 1 | Adopted |
| `git log --oneline` | View commit history (compact) | 3 | Learning |
| `git diff` | View unstaged changes | 4 | Not Introduced |

**Pattern Details:**

```bash
# git status
# Basic pattern
git status

# Translation: "Show me what's changed, staged, and untracked"

# Common use: Run before and after every git operation
```

```bash
# git log variations
# Basic pattern
git log --oneline

# Real example
git log --oneline -10
# Translation: "Show last 10 commits, one line each"

# Variations
git log --oneline --graph          # Show branch structure
git log --oneline --author="name"  # Filter by author
git log --since="2 weeks ago"      # Filter by time
```

```bash
# git diff
# Basic pattern
git diff                  # Unstaged changes
git diff --staged         # Staged changes (ready to commit)
git diff HEAD~1           # Compare to previous commit

# Translation: "Show me exactly what changed, line by line"
```

---

#### Category: Branching & Merging

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `git branch` | List branches | 4 | Not Introduced |
| `git branch <name>` | Create branch | 4 | Not Introduced |
| `git checkout <branch>` | Switch branches | 4 | Not Introduced |
| `git switch <branch>` | Switch branches (modern) | 4 | Not Introduced |
| `git checkout -b <name>` | Create and switch | 4 | Not Introduced |
| `git merge <branch>` | Merge branch into current | 4 | Not Introduced |
| `git branch -d <name>` | Delete branch | 4 | Not Introduced |

**Pattern Details:**

```bash
# Branch workflow
# Basic pattern
git checkout -b feature-name    # Create and switch to new branch
# ... make changes ...
git add .
git commit -m "Add feature"
git checkout main               # Switch back to main
git merge feature-name          # Merge feature into main
git branch -d feature-name      # Delete feature branch

# Translation: "Create isolated workspace, make changes, bring them back to main"
```

```bash
# git switch (modern alternative to checkout for branches)
# Basic pattern
git switch branch-name          # Switch to existing branch
git switch -c new-branch        # Create and switch (like checkout -b)

# Translation: "Clearer syntax — switch is only for branches, checkout does multiple things"
```

```bash
# Viewing branches
git branch                      # List local branches
git branch -a                   # List all (including remote)
git branch -v                   # List with last commit info

# Translation: "See what branches exist and which one I'm on"
```

---

#### Category: Undoing & Fixing

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `git restore <file>` | Discard unstaged changes | 4 | Not Introduced |
| `git restore --staged <file>` | Unstage file | 4 | Not Introduced |
| `git reset HEAD~1` | Undo last commit (keep changes) | 5 | Not Introduced |
| `git reset --hard HEAD~1` | Undo last commit (discard changes) | 5 | Not Introduced |
| `git revert <commit>` | Create new commit undoing changes | 5 | Not Introduced |
| `git stash` | Temporarily save uncommitted work | 4 | Not Introduced |
| `git stash pop` | Restore stashed work | 4 | Not Introduced |

**Pattern Details:**

```bash
# git restore (modern replacement for checkout -- file)
# Basic pattern
git restore filename.py         # Discard changes to file
git restore --staged filename.py  # Unstage file (keep changes)
git restore .                   # Discard all unstaged changes

# Translation: "Undo changes I haven't committed yet"
```

```bash
# git reset
# Basic pattern
git reset HEAD~1                # Undo last commit, keep changes staged
git reset --soft HEAD~1         # Undo last commit, keep changes staged
git reset --mixed HEAD~1        # Undo last commit, unstage changes (default)
git reset --hard HEAD~1         # Undo last commit, DELETE changes

# Translation: "Move back in history — soft/mixed are safe, hard is destructive"

# DANGER: --hard permanently deletes uncommitted work
```

```bash
# git stash
# Basic pattern
git stash                       # Save current work
git stash pop                   # Restore and remove from stash
git stash list                  # See all stashes
git stash apply                 # Restore but keep in stash

# Translation: "Put my work aside temporarily, come back to it later"

# Common use: Need to switch branches but have uncommitted work
git stash
git checkout other-branch
# ... do work ...
git checkout original-branch
git stash pop
```

---

#### Category: Remote Operations

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `git remote -v` | View remote URLs | 3 | Not Introduced |
| `git fetch` | Download remote changes (don't merge) | 4 | Not Introduced |
| `git pull --rebase` | Pull with rebase instead of merge | 5 | Not Introduced |
| `git push -u origin <branch>` | Push new branch to remote | 4 | Not Introduced |
| `git clone <url>` | Download repository | 1 | Adopted |

**Pattern Details:**

```bash
# git fetch vs pull
git fetch                       # Download changes, don't apply
git pull                        # Download AND merge (fetch + merge)

# Translation: "Fetch is safe peek, pull actually changes your code"

# When to use fetch:
git fetch
git log HEAD..origin/main --oneline   # See what's new before merging
git merge origin/main                  # Then merge if you want
```

```bash
# Push new branch
# Basic pattern
git push -u origin branch-name

# Translation: "Push this branch to remote and remember the connection"
# -u (--set-upstream) means future pushes just need 'git push'
```

---

### MEDIUM PRIORITY — Professional Competence

These patterns strengthen workflow and appear in collaborative environments. Should reach "Adopted" by Module 6.

---

#### Category: History & Investigation

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `git show <commit>` | View specific commit details | 5 | Not Introduced |
| `git blame <file>` | See who changed each line | 6 | Not Introduced |
| `git log -p` | Log with full diffs | 5 | Not Introduced |
| `git reflog` | View all HEAD movements | 6 | Not Introduced |

**Pattern Details:**

```bash
# git blame
# Basic pattern
git blame filename.py

# Translation: "Show me who wrote each line and when"

# Common use: Understanding why code exists, finding who to ask about it
```

```bash
# git reflog (recovery tool)
# Basic pattern
git reflog

# Translation: "Show every place HEAD has been — even 'deleted' commits"

# Recovery use:
git reflog                      # Find the commit hash you want
git checkout <hash>             # Go back to it
# Or: git reset --hard <hash>   # Reset to it
```

---

#### Category: Merge Conflict Resolution

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| Conflict markers | `<<<<<<<`, `=======`, `>>>>>>>` | 5 | Not Introduced |
| `git merge --abort` | Cancel merge in progress | 5 | Not Introduced |
| `git checkout --ours <file>` | Keep our version | 5 | Not Introduced |
| `git checkout --theirs <file>` | Keep their version | 5 | Not Introduced |

**Pattern Details:**

```bash
# Conflict markers
<<<<<<< HEAD
your changes here
=======
their changes here
>>>>>>> branch-name

# Translation: "Git couldn't auto-merge — you pick what to keep"

# Resolution steps:
1. Open file, find markers
2. Edit to keep what you want (remove markers)
3. git add <file>
4. git commit
```

```bash
# Abort if overwhelmed
git merge --abort               # Cancel and go back to before merge

# Translation: "Nevermind, undo the merge attempt"
```

---

#### Category: Rewriting History (Use with Caution)

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `git commit --amend` | Modify last commit | 5 | Not Introduced |
| `git rebase <branch>` | Replay commits on new base | 6 | Not Introduced |
| `git rebase -i HEAD~n` | Interactive rebase | 7 | Not Introduced |
| `git cherry-pick <commit>` | Copy specific commit | 6 | Not Introduced |

**Pattern Details:**

```bash
# git commit --amend
# Basic pattern
git commit --amend -m "New message"     # Change last commit message
git add forgotten-file.py
git commit --amend --no-edit            # Add file to last commit

# Translation: "Fix the last commit before pushing"

# WARNING: Don't amend commits already pushed to shared branches
```

```bash
# git rebase (basic)
# Basic pattern
git checkout feature-branch
git rebase main

# Translation: "Replay my commits on top of latest main"

# Result: Linear history instead of merge commits
# WARNING: Don't rebase commits already pushed to shared branches
```

---

### LOWER PRIORITY — Recognition & Reference

These patterns should be recognizable. Full fluency not required until needed.

---

#### Category: Tags & Releases

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `git tag <name>` | Create lightweight tag | 7 | Not Introduced |
| `git tag -a <name> -m "msg"` | Create annotated tag | 7 | Not Introduced |
| `git push --tags` | Push tags to remote | 7 | Not Introduced |

---

#### Category: Advanced Configuration

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `.gitignore` patterns | Ignore files/folders | 1 | Adopted |
| `git config --global` | Set global settings | 1 | Adopted |
| `git config --local` | Set repo-specific settings | 5 | Not Introduced |
| `.gitkeep` convention | Keep empty directories | 2 | Adopted |

---

## Bash Pattern Catalog

### HIGH PRIORITY — Daily Professional Use

---

#### Category: Navigation

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `cd` | Change directory | 1 | Adopted |
| `cd ..` | Go up one level | 1 | Adopted |
| `cd ~` | Go to home directory | 1 | Adopted |
| `cd -` | Go to previous directory | 3 | Not Introduced |
| `pwd` | Print working directory | 1 | Adopted |
| `ls` | List files | 1 | Adopted |
| `ls -la` | List all with details | 1 | Adopted |

**Pattern Details:**

```bash
# cd -
# Basic pattern
cd /some/long/path
cd /another/place
cd -                            # Goes back to /some/long/path

# Translation: "Toggle between last two directories"
```

```bash
# ls variations
ls                              # Basic list
ls -l                           # Long format (permissions, size, date)
ls -a                           # Show hidden files (dotfiles)
ls -la                          # Both
ls -lh                          # Human-readable sizes (KB, MB)
ls -lt                          # Sort by time (newest first)

# Translation: "See what's in this folder with varying detail"
```

---

#### Category: File Operations

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `touch <file>` | Create empty file | 1 | Adopted |
| `mkdir <dir>` | Create directory | 1 | Adopted |
| `mkdir -p <path>` | Create nested directories | 2 | Adopted |
| `cp <src> <dst>` | Copy file | 2 | Adopted |
| `cp -r <src> <dst>` | Copy directory | 3 | Not Introduced |
| `mv <src> <dst>` | Move/rename | 2 | Adopted |
| `rm <file>` | Remove file | 2 | Adopted |
| `rm -r <dir>` | Remove directory | 2 | Adopted |
| `rm -rf <dir>` | Force remove (DANGEROUS) | 3 | Not Introduced |

**Pattern Details:**

```bash
# mkdir -p
# Basic pattern
mkdir -p path/to/nested/folder

# Translation: "Create all folders in path, don't error if they exist"
```

```bash
# rm -rf WARNING
rm -rf directory/               # Deletes everything, no confirmation

# Translation: "Nuclear option — use with extreme caution"
# NEVER: rm -rf / or rm -rf * without checking pwd first
```

---

#### Category: Viewing Files

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `cat <file>` | Print entire file | 1 | Adopted |
| `head <file>` | Print first 10 lines | 3 | Not Introduced |
| `head -n 20 <file>` | Print first n lines | 3 | Not Introduced |
| `tail <file>` | Print last 10 lines | 3 | Not Introduced |
| `tail -f <file>` | Follow file (live updates) | 5 | Not Introduced |
| `less <file>` | Scrollable file viewer | 3 | Not Introduced |
| `wc -l <file>` | Count lines | 4 | Not Introduced |

**Pattern Details:**

```bash
# head and tail
head -n 5 data.csv              # First 5 lines
tail -n 5 data.csv              # Last 5 lines
tail -f logfile.log             # Watch log in real-time (Ctrl+C to exit)

# Translation: "Peek at beginning or end without opening whole file"
```

```bash
# less (pager)
less largefile.txt

# Navigation inside less:
# Space = next page
# b = previous page
# / = search
# q = quit

# Translation: "Read file without loading it all into memory"
```

---

#### Category: Piping & Redirection

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `cmd > file` | Write output to file (overwrite) | 3 | Not Introduced |
| `cmd >> file` | Append output to file | 3 | Not Introduced |
| `cmd1 \| cmd2` | Pipe output to next command | 4 | Not Introduced |
| `cmd < file` | Use file as input | 5 | Not Introduced |

**Pattern Details:**

```bash
# Redirection
echo "hello" > file.txt         # Create/overwrite file with "hello"
echo "world" >> file.txt        # Append "world" to file

# Translation: > is "write to", >> is "add to"
```

```bash
# Piping
# Basic pattern
command1 | command2 | command3

# Real examples
cat file.txt | grep "error"                    # Find lines with "error"
ls -la | head -5                               # First 5 items in listing
history | grep "git" | tail -10                # Last 10 git commands

# Translation: "Take output of left, feed it as input to right"
```

---

#### Category: Search & Filter

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `grep <pattern> <file>` | Search for pattern | 4 | Not Introduced |
| `grep -r <pattern> <dir>` | Recursive search | 4 | Not Introduced |
| `grep -i` | Case-insensitive | 4 | Not Introduced |
| `grep -n` | Show line numbers | 4 | Not Introduced |
| `find <dir> -name <pattern>` | Find files by name | 5 | Not Introduced |

**Pattern Details:**

```bash
# grep
# Basic pattern
grep "search_term" filename.txt

# Real examples
grep "error" log.txt                    # Lines containing "error"
grep -i "error" log.txt                 # Case-insensitive
grep -n "error" log.txt                 # With line numbers
grep -r "TODO" ./src/                   # Search all files in directory
grep -c "error" log.txt                 # Count matches

# Translation: "Find lines matching pattern"
```

```bash
# find
# Basic pattern
find <where> -name <what>

# Real examples
find . -name "*.py"                     # All Python files
find . -name "*.csv" -type f            # Only files, not directories
find . -mtime -7                        # Modified in last 7 days

# Translation: "Locate files matching criteria"
```

---

### MEDIUM PRIORITY — Professional Competence

---

#### Category: Environment & Variables

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `echo $VAR` | Print variable value | 4 | Not Introduced |
| `export VAR=value` | Set environment variable | 4 | Not Introduced |
| `env` | List all environment variables | 4 | Not Introduced |
| `$PATH` | Executable search path | 5 | Not Introduced |
| `which <cmd>` | Find command location | 3 | Not Introduced |
| `source <file>` | Run script in current shell | 5 | Not Introduced |

**Pattern Details:**

```bash
# Environment variables
export API_KEY="abc123"         # Set variable
echo $API_KEY                   # Print: abc123
unset API_KEY                   # Remove variable

# Translation: "Variables available to all commands in this session"
```

```bash
# which
which python                    # /usr/bin/python (or wherever it is)
which git                       # Find where command lives

# Translation: "What exactly runs when I type this command?"
```

```bash
# source (vs running script)
source ~/.bashrc                # Run in current shell, changes persist
./script.sh                     # Run in subshell, changes don't persist

# Translation: "source makes changes affect current terminal"
```

---

#### Category: Process Management

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `ps aux` | List all processes | 5 | Not Introduced |
| `top` / `htop` | Interactive process viewer | 5 | Not Introduced |
| `kill <pid>` | Terminate process | 5 | Not Introduced |
| `kill -9 <pid>` | Force kill | 5 | Not Introduced |
| `Ctrl+C` | Interrupt current command | 1 | Adopted |
| `Ctrl+Z` | Suspend current command | 5 | Not Introduced |
| `bg` / `fg` | Background/foreground job | 5 | Not Introduced |
| `cmd &` | Run in background | 5 | Not Introduced |

**Pattern Details:**

```bash
# Background processes
python long_script.py &         # Run in background
jobs                            # List background jobs
fg %1                           # Bring job 1 to foreground

# Translation: "Run something without blocking my terminal"
```

```bash
# Finding and killing processes
ps aux | grep python            # Find Python processes
kill 12345                      # Gracefully terminate PID 12345
kill -9 12345                   # Force kill (last resort)

# Translation: "Find what's running, stop it if needed"
```

---

#### Category: Permissions

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `chmod +x <file>` | Make executable | 4 | Not Introduced |
| `chmod 755 <file>` | Full permissions pattern | 6 | Not Introduced |
| `chown <user> <file>` | Change owner | 6 | Not Introduced |
| `sudo <cmd>` | Run as superuser | 3 | Learning |

**Pattern Details:**

```bash
# chmod basics
chmod +x script.sh              # Make script executable
chmod -x script.sh              # Remove executable permission

# Translation: "Control who can read/write/execute this file"

# Numeric permissions (advanced):
# 7 = read + write + execute
# 5 = read + execute
# 4 = read only
chmod 755 script.sh             # Owner: all, Others: read+execute
```

---

### LOWER PRIORITY — Recognition & Reference

---

#### Category: Text Processing

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `sort` | Sort lines | 6 | Not Introduced |
| `uniq` | Remove duplicate lines | 6 | Not Introduced |
| `cut` | Extract columns | 6 | Not Introduced |
| `sed` | Stream editor | 7 | Not Introduced |
| `awk` | Pattern processing | 7 | Not Introduced |

---

#### Category: Networking

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `curl <url>` | HTTP requests | 4 | Not Introduced |
| `wget <url>` | Download files | 4 | Not Introduced |
| `ssh user@host` | Remote connection | 9 | Not Introduced |
| `scp <src> <dst>` | Secure copy | 9 | Not Introduced |

---

#### Category: Compression

| Pattern | Description | Module Intro | Status |
|---------|-------------|--------------|--------|
| `zip -r <name> <dir>` | Create zip | 5 | Not Introduced |
| `unzip <file>` | Extract zip | 5 | Not Introduced |
| `tar -czf <name> <dir>` | Create tar.gz | 6 | Not Introduced |
| `tar -xzf <file>` | Extract tar.gz | 6 | Not Introduced |

---

## Tracking Summary Table

**Status Legend:**
- **Not Introduced:** Haven't covered yet
- **Learning:** Currently drilling
- **Adopted:** Can use without reference
- **Maintenance Pool:** In rotation to prevent decay

### Git Status

| Category | Adopted | Learning | Not Introduced |
|----------|---------|----------|----------------|
| Core Workflow | status, add, commit, push, pull, clone | log --oneline | diff |
| Branching | — | — | All |
| Undoing | — | — | All |
| Remote | clone | — | fetch, push -u |
| History | — | — | All |
| Conflicts | — | — | All |

### Bash Status

| Category | Adopted | Learning | Not Introduced |
|----------|---------|----------|----------------|
| Navigation | cd, pwd, ls, ls -la | — | cd - |
| File Ops | touch, mkdir, cp, mv, rm | — | cp -r, rm -rf |
| Viewing | cat | — | head, tail, less |
| Piping | — | — | All |
| Search | — | — | All |
| Environment | — | — | All |
| Permissions | Ctrl+C | sudo | chmod, kill |

---

## Module Alignment (Proposed)

### Module 4 — API Integration
**Git:** Branching basics, stash, push -u, diff
**Bash:** Piping, grep, environment variables, curl

### Module 5 — Advanced ML
**Git:** reset, revert, merge conflicts, commit --amend
**Bash:** head/tail, find, process management, chmod

### Module 6 — NLP
**Git:** rebase basics, cherry-pick, blame
**Bash:** Text processing basics (sort, uniq, cut)

### Module 9 — Deployment & MLOps
**Git:** Tags, advanced remote operations
**Bash:** SSH/SCP, compression, full process management

---

## Critical Reminders for Claude

**When integrating Git/Bash into warmups (future):**
1. Check this document for scheduled patterns
2. Check status column — don't re-introduce Adopted patterns as new
3. Use teaching format: Pattern → Example → Translation → Variations
4. Git patterns: Always note destructive commands (reset --hard, rm -rf)
5. Bash patterns: Note platform differences if relevant (macOS vs Linux)

**When user asks about unfamiliar command:**
1. Check if it's in this catalog
2. If yes, use teaching format and mark as "Learning"
3. If no, add it to appropriate category

---

## End of Git & Bash Patterns Master

**This document is the source of truth for command line fluency curriculum.**

**Referenced by:** Daily workflow structure (future), module planning docs  
**Updated when:** Patterns change status, new patterns identified  
**Integration planned:** Module 4

---

**Last Updated:** January 3, 2026  
**Current Module:** 4  
**Integration Status:** Active — supplemental curriculum
