# 📤 GitHub Upload Guide

## 🎯 Quick Steps to Upload Your Project

### Step 1: Install Git (if not already installed)

Download and install Git from: https://git-scm.com/download/win

### Step 2: Initialize Git Repository

Open PowerShell in your project folder and run:

```powershell
# Navigate to project directory
cd "C:\Users\shreya\OneDrive\Desktop\DJANGO_PROJECT\django(@)\django(2)"

# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Attendance Manager project"
```

### Step 3: Create GitHub Repository

1. Go to https://github.com
2. Click "New repository" (green button)
3. Enter repository name: `attendance-manager`
4. Choose "Public" or "Private"
5. **DO NOT** check "Initialize with README" (you already have one)
6. Click "Create repository"

### Step 4: Connect and Push to GitHub

GitHub will show you commands. Use these:

```powershell
# Add remote repository (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/attendance-manager.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

---

## 🔐 Important: Protect Sensitive Information

### Files That Are Protected (Already in .gitignore):

✅ `.env` - Contains database password
✅ `venv/` - Virtual environment (too large)
✅ `__pycache__/` - Python cache files
✅ `*.pyc` - Compiled Python files
✅ `db.sqlite3` - Database file
✅ `*.log` - Log files
✅ `backups/` - Backup files

### What Gets Uploaded:

✅ Source code (`.py`, `.html`, `.js`, `.css`)
✅ Documentation (`.md` files)
✅ Configuration templates (`.env.example`)
✅ Requirements (`requirements.txt`)
✅ Scripts and batch files

---

## 📋 Before Uploading Checklist

- [ ] `.gitignore` file is created
- [ ] `.env` file contains your sensitive data (will NOT be uploaded)
- [ ] `.env.example` file is created (will be uploaded as template)
- [ ] Database password is in `.env`, not in `settings.py`
- [ ] `venv/` folder will be ignored
- [ ] `README.md` is complete and informative

---

## 🔧 Update settings.py to Use Environment Variables

To make your project more secure, update `settings.py` to read from `.env`:

### Step 1: Install python-decouple

```powershell
.\venv\Scripts\Activate.ps1
pip install python-decouple
pip freeze > requirements.txt
```

### Step 2: Update settings.py

Add at the top of `settings.py`:

```python
from decouple import config

# Replace hardcoded values with:
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```

---

## 📝 Complete Git Commands Reference

### Initial Setup

```powershell
# Configure git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Add remote
git remote add origin https://github.com/YOUR-USERNAME/attendance-manager.git

# Push
git push -u origin main
```

### Making Updates Later

```powershell
# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push
```

### Useful Commands

```powershell
# View commit history
git log

# View remote URL
git remote -v

# Check which files will be committed
git status

# See what changed
git diff

# Undo changes (before commit)
git checkout -- filename

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main
```

---

## 🌐 Clone Your Project on Another Computer

Once uploaded to GitHub, anyone (or you on another computer) can clone it:

```powershell
# Clone repository
git clone https://github.com/YOUR-USERNAME/attendance-manager.git

# Navigate to project
cd attendance-manager

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file (copy from .env.example and fill in values)
copy .env.example .env
# Edit .env with your database credentials

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## 📄 Create a Good README for GitHub

Your `README.md` should include:

1. **Project Title and Description**
2. **Features**
3. **Screenshots** (optional but recommended)
4. **Installation Instructions**
5. **Usage Instructions**
6. **Technologies Used**
7. **Contributing Guidelines** (optional)
8. **License** (optional)

Your current `README.md` already has most of this!

---

## 🖼️ Add Screenshots (Optional)

To make your GitHub repo more attractive:

1. Take screenshots of your app
2. Create a `screenshots/` folder
3. Add images to the folder
4. Reference them in README.md:

```markdown
## Screenshots

![Login Page](screenshots/login.png)
![Dashboard](screenshots/dashboard.png)
![Calendar View](screenshots/calendar.png)
```

---

## 🔒 Security Best Practices

### Never Upload These:

❌ Database passwords
❌ Secret keys
❌ API keys
❌ Personal information
❌ `.env` file
❌ Database files

### Always Upload These:

✅ Source code
✅ Documentation
✅ `.env.example` (template)
✅ `requirements.txt`
✅ `.gitignore`

---

## 🚨 If You Accidentally Uploaded Sensitive Data

If you accidentally committed sensitive information:

```powershell
# Remove file from git but keep locally
git rm --cached .env

# Commit the removal
git commit -m "Remove sensitive file"

# Push changes
git push

# Then change your passwords immediately!
```

---

## 📊 GitHub Repository Settings

After uploading, configure your repository:

1. **Add Description:** Short description of your project
2. **Add Topics:** `django`, `python`, `attendance`, `postgresql`
3. **Add README:** Already done!
4. **Choose License:** MIT, Apache, etc. (optional)
5. **Enable Issues:** For bug tracking
6. **Enable Wiki:** For documentation (optional)

---

## 🎓 For Your Teacher/Presentation

When sharing your GitHub repository:

1. **Make it Public** (so teacher can view)
2. **Add a good README** with:
   - Project description
   - How to run
   - Features
   - Screenshots
3. **Clean commit history** with meaningful messages
4. **Add a LICENSE** file (optional)

### Share This URL:
```
https://github.com/YOUR-USERNAME/attendance-manager
```

---

## 💡 Pro Tips

1. **Commit Often:** Make small, frequent commits with clear messages
2. **Write Good Commit Messages:** 
   - ✅ "Add user authentication feature"
   - ❌ "Update files"
3. **Use Branches:** For new features, create a branch
4. **Keep README Updated:** Update documentation as you add features
5. **Add .gitignore Early:** Before first commit

---

## 🆘 Troubleshooting

### "Permission denied (publickey)"

**Solution:** Use HTTPS instead of SSH:
```powershell
git remote set-url origin https://github.com/YOUR-USERNAME/attendance-manager.git
```

### "Repository not found"

**Solution:** Check the URL is correct:
```powershell
git remote -v
```

### "Failed to push"

**Solution:** Pull first, then push:
```powershell
git pull origin main --rebase
git push origin main
```

### Large files error

**Solution:** Make sure `venv/` is in `.gitignore`

---

## 📚 Additional Resources

- **Git Documentation:** https://git-scm.com/doc
- **GitHub Guides:** https://guides.github.com/
- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf

---

**Ready to upload? Follow the steps above and your project will be on GitHub!** 🚀
