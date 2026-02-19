# 🚀 Deploy to PythonAnywhere (FREE) - Step-by-Step Guide

**PythonAnywhere** = Free hosting with instant public URL for your Adruva Creation website!

---

## **Step 1: Create Free PythonAnywhere Account**

1. Go to https://www.pythonanywhere.com
2. Click **Sign Up**
3. Choose **Free Account** (Beginner tier)
4. Fill in details and create account
5. **Verify email**

---

## **Step 2: Add GitHub Repository**

1. Login to PythonAnywhere dashboard
2. Click **Consoles** → **Bash**
3. Run this command:

```bash
git clone https://github.com/hero1749t/Adruva-creation.git
```

This clones your entire project!

---

## **Step 3: Create Virtual Environment**

Still in Bash console:

```bash
cd Adruva-creation
mkvirtualenv --python=/usr/bin/python3.10 adruva
pip install -r requirements.txt
python manage.py migrate
```

---

## **Step 4: Configure Web App**

1. Click **Web** (left sidebar)
2. Click **Add a new web app**
3. Choose domain: `your-username.pythonanywhere.com`
4. Click **Next**
5. Select **Django**
6. Choose **Python 3.10**
7. Click **Next**

---

## **Step 5: Update WSGI Configuration**

1. In **Web** tab, scroll down to **WSGI configuration file**
2. Click the file path (like: `/home/username/mysite.com_wsgi.py`)
3. **Replace entire content** with this:

```python
import os
import sys

path = '/home/{username}/Adruva-creation'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'agency.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

⚠️ **Replace `{username}` with your PythonAnywhere username!**

---

## **Step 6: Configure Static Files**

1. Back in **Web** tab
2. Scroll to **Static files and directories**
3. Click **Enter URL path and directory location:**

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/{username}/Adruva-creation/static` |
| `/media/` | `/home/{username}/Adruva-creation/media` |

⚠️ Again, replace `{username}`!

---

## **Step 7: Update Django Settings**

1. Go to **Files** tab
2. Navigate: `Adruva-creation` → `agency` → `settings.py`
3. Find `ALLOWED_HOSTS` and update:

```python
ALLOWED_HOSTS = ['*', 'your-username.pythonanywhere.com']
```

4. Set `DEBUG = False` at the top
5. Save file

---

## **Step 8: Reload Web App**

1. Go back to **Web** tab
2. Click green **Reload** button at top
3. Wait 30 seconds...

---

## **🎉 Your Website is LIVE!**

Your public URL:
```
https://your-username.pythonanywhere.com
```

**Share this link with your friend!** ✨

---

## **Admin Panel**

Access admin at:
```
https://your-username.pythonanywhere.com/admin
```

**Default admin:**
- Username: `admin`
- Password: Set with: `python manage.py createsuperuser`

---

## **Troubleshooting**

### **Error: Module not found**
- Run in Bash: `pip install -r requirements.txt`
- Reload web app

### **Static files not showing**
- Run: `python manage.py collectstatic`
- Reload web app

### **Database errors**
- Run: `python manage.py migrate`
- Reload web app

---

## **Share with Your Friend**

Once deployed, your friend can:
1. **Open directly:** `https://your-username.pythonanywhere.com`
2. **No installation needed**
3. **Always available**

---

**Total time: ~10 minutes!** ⏱️
