# How to Commit and Push Changes

Use these steps each time you want to save your work to GitHub.

## 1. Open terminal in the project root

```bash
cd "/workspaces/AH-CompSci-SDD-Python"
```

## 2. Check what changed

```bash
git status --short
```

This shows:
- `M` modified files
- `A` added files
- `D` deleted files
- `??` untracked files

## 3. Add files to the commit

Add everything:

```bash
git add -A
```

Or add one file:

```bash
git add "README.md"
```

## 4. Commit with a clear message

```bash
git commit -m "Short clear summary of changes"
```

Good commit messages:
- `Reorganize Booklet 3 into program folders`
- `Add task files for Program 20 to Program 22`
- `Update README Codespaces setup instructions`

## 5. Push to GitHub

```bash
git push origin main
```

## 6. Confirm push worked

```bash
git status
```

Expected result:

`nothing to commit, working tree clean`

## Quick full workflow

```bash
cd "/workspaces/AH-CompSci-SDD-Python"
git status --short
git add -A
git commit -m "Describe your update"
git push origin main
```

## Common issues

### "nothing to commit"
You have not changed any files, or your changes are not saved.

### "failed to push" or "non-fast-forward"
Pull latest changes first, then push again:

```bash
git pull --rebase origin main
git push origin main
```

### "Author identity unknown"
Set your Git name/email once:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
