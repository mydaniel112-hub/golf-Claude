# Connect to Railway via Terminal

## Step 1: Install Railway CLI

```bash
npm install -g @railway/cli
```

If you don't have npm, install it first:
```bash
brew install node
```

## Step 2: Login to Railway

```bash
railway login
```

This will open a browser to authenticate.

## Step 3: Initialize Railway Project

```bash
cd "/Users/danielmacwilliams/gold claude"
railway init
```

Follow the prompts:
- Create new project? Yes
- Project name: golf-claude (or whatever you want)

## Step 4: Link to Existing Project (if needed)

If you already created a project on Railway website:
```bash
railway link
```

Then select your project from the list.

## Step 5: Deploy

```bash
railway up
```

This will deploy your code to Railway!

---

## Alternative: Use Railway Web Interface

Actually, it's easier to just use the Railway website:
1. Go to https://railway.app
2. Click "New Project"
3. Click "Deploy from GitHub repo"
4. Select your `golf-Claude` repo

No terminal needed!
