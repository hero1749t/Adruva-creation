# ⚡ FASTEST PYTHONANYWHERE DEPLOYMENT - 5 MINUTES!

## **COPY & PASTE THESE COMMANDS**

### **Step 1: Create Free Account (1 min)**
- Go to https://www.pythonanywhere.com
- Click **Sign Up**
- Choose **Free Account**
- Verify email

---

### **Step 2: Run Deployment Script (2 min)**

Go to **Consoles** → **Bash** and paste this:

```bash
cd ~ && bash <(curl -s https://raw.githubusercontent.com/hero1749t/Adruva-creation/main/deploy_pythonanywhere.sh)
```

**OR run these commands one by one:**

```bash
cd ~
git clone https://github.com/hero1749t/Adruva-creation.git
cd Adruva-creation
mkvirtualenv --python=/usr/bin/python3.10 adruva
source ~/.virtualenvs/adruva/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@adruva.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell
```

---

### **Step 3: Get Your Username (30 sec)**

In the same bash console, type:
```bash
whoami
```

Copy the output (your username)

---

### **Step 4: Create Web App (1 min)**

1. Click **Web** (left sidebar)
2. Click **Add a new web app**
3. Enter: `{USERNAME}.pythonanywhere.com` (replace {USERNAME})
4. Click **Next**
5. Select **Django**
6. Choose **Python 3.10**
7. Click **Next**

---

### **Step 5: Update WSGI File (1 min)**

1. Still in **Web** tab
2. Scroll to **WSGI configuration file**
3. Click the file path to edit it
4. **Delete all content** and paste this:

```python
import os
import sys

path = '/home/{USERNAME}/Adruva-creation'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'agency.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

⚠️ **Replace `{USERNAME}` with your actual username!**

5. Click **Save**

---

### **Step 6: Set Static Files (1 min)**

1. Back in **Web** tab
2. Scroll to **Static files and directories**
3. Add these mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/{USERNAME}/Adruva-creation/static` |
| `/media/` | `/home/{USERNAME}/Adruva-creation/media` |

---

### **Step 7: Reload & Done! (30 sec)**

1. Click the green **Reload** button
2. Wait 30 seconds
3. Open your browser: `https://{USERNAME}.pythonanywhere.com`

---

## ✨ **YOUR SITE IS LIVE!**

| Link | Use |
|------|-----|
| `https://{USERNAME}.pythonanywhere.com` | **Main website** 🌐 |
| `https://{USERNAME}.pythonanywhere.com/admin` | **Admin panel** 📧 |
| **Username:** `admin` | **Default login** |
| **Password:** `admin123` | **Default password** |

---

## 🎯 TROUBLESHOOTING

### **Website shows error?**
- Click **Reload** button again
- Wait 30 seconds
- Refresh browser

### **Static files (CSS/images) not showing?**
In **Bash** console:
```bash
cd ~/Adruva-creation
python manage.py collectstatic --noinput
```
Then click **Reload**

### **Admin login not working?**
In **Bash** console:
```bash
cd ~/Adruva-creation
source ~/.virtualenvs/adruva/bin/activate
python manage.py changepassword admin
```

---

**Total time: 5-10 minutes! 🚀**
