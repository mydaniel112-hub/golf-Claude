# Push to GitHub - Commands

## Step 1: Initialize Git (if not already done)
```bash
cd "/Users/danielmacwilliams/gold claude"
git init
```

## Step 2: Add all files
```bash
git add .
```

## Step 3: Make first commit
```bash
git commit -m "Initial commit: Golf ball tracker with real-time web interface"
```

## Step 4: Create GitHub repository
1. Go to https://github.com/new
2. Create a new repository (don't initialize with README)
3. Copy the repository URL

## Step 5: Add remote and push
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` and `YOUR_REPO_NAME` with your actual GitHub username and repo name.

---

## All-in-One Commands:
```bash
cd "/Users/danielmacwilliams/gold claude"
git init
git add .
git commit -m "Initial commit: Golf ball tracker"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```
