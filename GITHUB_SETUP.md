# 📤 GitHub Setup & Push Instructions

Follow these steps to push your Adruva Creation project to GitHub and share with your friend.

## Step 1: Create GitHub Repository

1. Go to [github.com](https://github.com) and log in
2. Click **+** (top right) → **New repository**
3. Fill in:
   - **Repository name:** `adruva-creation` (or your preferred name)
   - **Description:** `Digital Marketing Agency Website - Django`
   - **Visibility:** Public (so friends can view)
   - Do NOT initialize with README (we already have one)
4. Click **Create repository**

## Step 2: Add Remote & Push Code

After creating the repo, you'll see commands. Replace `YOUR_USERNAME` with your GitHub username and run:

```bash
cd "c:\Users\deepu\Downloads\Documents\Adruva_creation\New folder (4)"
git add .
git commit -m "Initial commit: Adruva Creation marketing agency website"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/adruva-creation.git
git push -u origin main
```

## Step 3: Share with Your Friend

Once pushed, share this link with your friend:
```
https://github.com/YOUR_USERNAME/adruva-creation
```

Your friend can then:

### Clone & Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/adruva-creation.git
cd adruva-creation
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Then open: **http://127.0.0.1:8000**

### Collaborate on GitHub

1. **Fork** your repository (on GitHub)
2. Clone their fork locally
3. Make changes
4. Push to their fork
5. Create **Pull Request** back to main repo

## Step 4 (Optional): Add Collaborators

If you want your friend to have direct access:

1. Go to your GitHub repo
2. Click **Settings** → **Collaborators**
3. Click **Add people**
4. Search for your friend's GitHub username
5. They'll get an invite to join

## ✅ Checklist Before Pushing

- [ ] All files committed (`git status` should be clean)
- [ ] `.gitignore` excludes `.venv`, `db.sqlite3`, `*.pyc`, `__pycache__`
- [ ] `README.md` has clear setup instructions
- [ ] `requirements.txt` is updated
- [ ] No sensitive data (SECRET_KEY, passwords) in code

## 🔄 Regular Updates

After initial push, to update GitHub with new changes:

```bash
git add .
git commit -m "Your commit message describing changes"
git push origin main
```

## 📊 GitHub Features Your Friend Can Use

- **Issues:** Report bugs or request features
- **Projects:** Kanban board for task management
- **Discussions:** Chat about the project
- **Pull Requests:** Suggest changes
- **Wiki:** Documentation

---

**Next Steps:**
1. Create the repository on GitHub
2. Run the git commands above
3. Share the repository link with your friend
4. They can fork, clone, and start working!
