# ✅ GitHub Upload Checklist

## Before Uploading - Check These:

### 1. Sensitive Files Protected
- [ ] `.gitignore` file exists
- [ ] `.env` is listed in `.gitignore`
- [ ] Database password is in `.env` (not in settings.py)
- [ ] `.env.example` has placeholder text (not real password)

### 2. Large Files Excluded
- [ ] `venv/` is in `.gitignore`
- [ ] `__pycache__/` is in `.gitignore`
- [ ] `backups/` is in `.gitignore`

### 3. Documentation Ready
- [ ] `README.md` is complete
- [ ] `requirements.txt` is updated
- [ ] Project description is clear

### 4. Test Before Upload
```powershell
# Check what will be uploaded
git status

# Make sure .env is NOT listed
# Make sure venv/ is NOT listed
```

---

## Upload Steps

### Step 1: Initialize Git
```powershell
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
git init
```

### Step 2: Add Files
```powershell
git add .
```

### Step 3: Check What's Added
```powershell
git status
```

**STOP! Check this list:**
- ✅ Should see: .py, .html, .js, .css, .md files
- ❌ Should NOT see: .env, venv/, __pycache__/

### Step 4: Commit
```powershell
git commit -m "Initial commit: Attendance Manager"
```

### Step 5: Create GitHub Repo
1. Go to https://github.com
2. Click "New repository"
3. Name: `attendance-manager`
4. Click "Create repository"

### Step 6: Push to GitHub
```powershell
# Replace YOUR-USERNAME
git remote add origin https://github.com/YOUR-USERNAME/attendance-manager.git
git branch -M main
git push -u origin main
```

---

## After Upload - Verify

### Check on GitHub:
- [ ] Source code is visible
- [ ] README.md displays correctly
- [ ] `.env` is NOT visible (should be missing)
- [ ] `venv/` is NOT visible (should be missing)
- [ ] `.env.example` IS visible (template)

---

## 🚨 If You See .env on GitHub

**DANGER!** Your password is public!

**Fix immediately:**
```powershell
# Remove from git
git rm --cached .env

# Commit removal
git commit -m "Remove sensitive file"

# Push
git push

# CHANGE YOUR DATABASE PASSWORD NOW!
```

---

## ✅ Success Indicators

You did it right if:
- ✅ Repository is created
- ✅ Source code is visible
- ✅ `.env` is NOT visible
- ✅ `venv/` is NOT visible
- ✅ README displays nicely
- ✅ No passwords visible anywhere

---

## 📝 Quick Reference

**What's Protected (NOT uploaded):**
- `.env` (password)
- `venv/` (too big)
- `__pycache__/` (cache)
- `*.pyc` (compiled)
- `backups/` (personal)
- `*.log` (logs)

**What's Uploaded:**
- Source code (.py, .html, .js, .css)
- Documentation (.md)
- `requirements.txt`
- `.env.example` (template)
- Scripts (.bat, .py)

---

**Print this checklist and check each item before uploading!** 📋
