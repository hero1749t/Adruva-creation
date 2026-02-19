#!/bin/bash
# 🚀 ADRUVA CREATION - AUTOMATED PYTHONANYWHERE DEPLOYMENT SCRIPT
# Run this in PythonAnywhere Bash Console to set up everything automatically!

echo "=========================================="
echo "🚀 ADRUVA CREATION AUTO-DEPLOYMENT"
echo "=========================================="
echo ""

# Step 1: Clone repository
echo "📦 Step 1: Cloning repository..."
cd ~
git clone https://github.com/hero1749t/Adruva-creation.git
cd Adruva-creation

# Step 2: Create virtual environment
echo "🔧 Step 2: Creating virtual environment..."
mkvirtualenv --python=/usr/bin/python3.10 adruva
source ~/.virtualenvs/adruva/bin/activate

# Step 3: Install dependencies
echo "📚 Step 3: Installing dependencies..."
pip install -r requirements.txt --quiet

# Step 4: Run migrations
echo "🗄️  Step 4: Running database migrations..."
python manage.py migrate

# Step 5: Create admin user (optional)
echo "👤 Step 5: Creating admin user..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@adruva.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Step 6: Collect static files
echo "🎨 Step 6: Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "=========================================="
echo "✅ DEPLOYMENT COMPLETE!"
echo "=========================================="
echo ""
echo "📋 Next Steps:"
echo "1. Go to PythonAnywhere Web tab"
echo "2. Click 'Add a new web app'"
echo "3. Select 'Django' + 'Python 3.10'"
echo "4. Update WSGI file with your username:"
echo ""
echo "   path = '/home/{USERNAME}/Adruva-creation'"
echo ""
echo "5. Set static files:"
echo "   /static/ -> /home/{USERNAME}/Adruva-creation/static"
echo "   /media/  -> /home/{USERNAME}/Adruva-creation/media"
echo ""
echo "6. Reload web app"
echo ""
echo "🌐 Your site: https://{USERNAME}.pythonanywhere.com"
echo "📧 Admin: https://{USERNAME}.pythonanywhere.com/admin"
echo "🔑 Login: admin / admin123"
echo ""
echo "=========================================="
