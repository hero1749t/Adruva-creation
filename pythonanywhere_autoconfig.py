#!/usr/bin/env python3
"""
COMPLETE PYTHONANYWHERE AUTO-DEPLOYMENT SCRIPT
Run this AFTER the bash script to configure WSGI and static files
"""

import os
import sys
import subprocess

def get_username():
    """Get PythonAnywhere username from home directory."""
    home = os.path.expanduser("~")
    return os.path.basename(home)

def create_wsgi_file(username):
    """Create proper WSGI configuration file."""
    
    wsgi_path = f'/home/{username}/Adruva-creation/wsgi_config.py'
    
    wsgi_content = f'''import os
import sys

# Add project to path
path = '/home/{username}/Adruva-creation'
if path not in sys.path:
    sys.path.append(path)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'agency.settings'

# Import WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''
    
    try:
        with open(wsgi_path, 'w') as f:
            f.write(wsgi_content)
        print(f"✅ WSGI file created: {wsgi_path}")
        return wsgi_path
    except Exception as e:
        print(f"❌ Error creating WSGI file: {e}")
        return None

def update_allowed_hosts(username):
    """Update ALLOWED_HOSTS in settings.py"""
    
    settings_path = f'/home/{username}/Adruva-creation/agency/settings.py'
    
    try:
        with open(settings_path, 'r') as f:
            content = f.read()
        
        # Replace ALLOWED_HOSTS
        old_hosts = "ALLOWED_HOSTS = [\"*\"]"
        new_hosts = f"ALLOWED_HOSTS = ['*', '{username}.pythonanywhere.com']"
        content = content.replace(old_hosts, new_hosts)
        
        # Set DEBUG to False
        content = content.replace("DEBUG = True", "DEBUG = False")
        
        with open(settings_path, 'w') as f:
            f.write(content)
        
        print(f"✅ Settings updated for {username}.pythonanywhere.com")
        return True
    except Exception as e:
        print(f"❌ Error updating settings: {e}")
        return False

def main():
    print("\n" + "="*60)
    print("🚀 PYTHONANYWHERE AUTO-CONFIGURATION")
    print("="*60 + "\n")
    
    username = get_username()
    print(f"👤 Detected username: {username}")
    print(f"🌐 Your domain will be: {username}.pythonanywhere.com\n")
    
    # Step 1: Create WSGI file
    print("Step 1: Creating WSGI configuration...")
    wsgi_path = create_wsgi_file(username)
    
    # Step 2: Update settings
    print("\nStep 2: Updating Django settings...")
    update_allowed_hosts(username)
    
    # Step 3: Collect static files
    print("\nStep 3: Collecting static files...")
    try:
        os.chdir(f'/home/{username}/Adruva-creation')
        subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'], 
                      capture_output=True)
        print("✅ Static files collected")
    except Exception as e:
        print(f"⚠️  Static files collection: {e}")
    
    print("\n" + "="*60)
    print("✅ AUTO-CONFIGURATION COMPLETE!")
    print("="*60 + "\n")
    
    print("📋 FINAL STEPS IN PYTHONANYWHERE WEB TAB:\n")
    print(f"1. Click 'Add a new web app'")
    print(f"2. Choose: {username}.pythonanywhere.com")
    print(f"3. Select: Django + Python 3.10")
    print(f"4. WSGI configuration file path:")
    print(f"   → /home/{username}/Adruva-creation/wsgi_config.py")
    print(f"\n5. Add Static files mapping:")
    print(f"   URL: /static/")
    print(f"   Directory: /home/{username}/Adruva-creation/static")
    print(f"\n   URL: /media/")
    print(f"   Directory: /home/{username}/Adruva-creation/media")
    print(f"\n6. Click the GREEN RELOAD button")
    print(f"\n{'='*60}")
    print(f"🌐 Website: https://{username}.pythonanywhere.com")
    print(f"📧 Admin:   https://{username}.pythonanywhere.com/admin")
    print(f"🔑 Login:   admin / admin123")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
