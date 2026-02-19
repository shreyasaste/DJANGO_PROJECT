# 🚀 Quick GitHub Upload Steps

## ⚡ 5-Minute Upload Guide

### 1️⃣ Open PowerShell in Project Folder

```powershell
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"
```

### 2️⃣ Initialize Git

```powershell
git init
git add .
git commit -m "Initial commit: Attendance Manager"
```

### 3️⃣ Create GitHub Repository

1. Go to https://github.com
2. Click "New repository"
3. Name: `attendance-manager`
4. Click "Create repository"

### 4️⃣ Push to GitHub

```powershell
# Replace YOUR-USERNAME with your GitHub username
git remote add origin https://github.com/YOUR-USERNAME/attendance-manager.git
git branch -M main
git push -u origin main
```

### 5️⃣ Done! 🎉

Your project is now on GitHub!

---

## 🔐 What's Protected?

These files will NOT be uploaded (they're in `.gitignore`):

- ✅ `.env` (your database password)
- ✅ `venv/` (virtual environment)
- ✅ `__pycache__/` (cache files)
- ✅ `*.pyc` (compiled files)
- ✅ `backups/` (backup files)

---

## 📝 Update Later

```powershell
git add .
git commit -m "Description of changes"
git push
```

---

## 🆘 Need Help?

See `GITHUB_UPLOAD_GUIDE.md` for detailed instructions!

---

**Your GitHub URL will be:**
```
https://github.com/YOUR-USERNAME/attendance-manager
```
