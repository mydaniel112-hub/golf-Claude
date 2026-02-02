# Connect Railway to Your Repo

## Important: Railway Doesn't Use Tokens

Railway connects to GitHub through **OAuth** (web login), not tokens. You don't need to give Railway a token.

## How to Connect Railway:

### Step 1: Go to Railway
Visit: https://railway.app

### Step 2: Sign In with GitHub
- Click "Start a New Project" or "Login"
- Choose **"Sign in with GitHub"**
- Authorize Railway to access your repos

### Step 3: Deploy Your Repo
- Click **"New Project"**
- Select **"Deploy from GitHub repo"**
- Find and click **`golf-Claude`**
- Railway automatically connects and deploys!

---

## Your New Token (For Git Operations)

I've updated your git remote to use the new token. You can now:
- Push to GitHub: `git push`
- Pull from GitHub: `git pull`

The token is saved in your git remote URL.

---

## Railway Auto-Deploys

Once Railway is connected to your GitHub repo:
- Every time you `git push`, Railway automatically rebuilds
- No manual steps needed!
- Your app stays up to date

---

## Next Steps:

1. **Go to Railway** and connect your repo (see steps above)
2. **Wait for deployment** (2-3 minutes)
3. **Get your URL** from Railway
4. **Open on iPhone** and start tracking!

No token needed for Railway - just sign in with GitHub!
