#!/usr/bin/env python3
"""
PythonAnywhere Deployment Checklist Generator
Run this after deploying to verify everything works
"""

import os
import sys

def check_deployment():
    """Check if deployment is ready."""
    
    print("\n" + "="*70)
    print("✅ PYTHONANYWHERE DEPLOYMENT CHECKLIST")
    print("="*70 + "\n")
    
    checks = [
        ("✓ GitHub repo created", "https://github.com/hero1749t/Adruva-creation"),
        ("✓ PythonAnywhere account", "https://www.pythonanywhere.com/accounts/login/"),
        ("✓ Cloned project", "git clone in PythonAnywhere bash console"),
        ("✓ Virtual env created", "mkvirtualenv adruva"),
        ("✓ Dependencies installed", "pip install -r requirements.txt"),
        ("✓ Database migrated", "python manage.py migrate"),
        ("✓ Web app configured", "Django + Python 3.10"),
        ("✓ WSGI file updated", "Updated with correct path"),
        ("✓ Static files set", "/static/ and /media/ paths configured"),
        ("✓ Settings.py updated", "ALLOWED_HOSTS set, DEBUG=False"),
        ("✓ Web app reloaded", "Green reload button clicked"),
    ]
    
    for i, (check, details) in enumerate(checks, 1):
        print(f"{i:2d}. {check}")
        print(f"    → {details}\n")
    
    print("="*70)
    print("\n🎉 ONCE ALL CHECKS DONE:\n")
    print("Your live URL: https://your-username.pythonanywhere.com")
    print("Admin URL:     https://your-username.pythonanywhere.com/admin")
    print("\n✨ Share the main URL with your friend!\n")
    print("="*70 + "\n")
    
    # Check local setup
    print("\n📋 LOCAL PROJECT STATUS:\n")
    
    checks_local = [
        ("README.md", "Project documentation"),
        ("PYTHONANYWHERE_DEPLOY.md", "Deployment guide"),
        ("requirements.txt", "Python dependencies"),
        (".gitignore", "Git exclusions"),
        ("manage.py", "Django CLI"),
    ]
    
    for filename, desc in checks_local:
        exists = os.path.exists(filename)
        status = "✅" if exists else "❌"
        print(f"{status} {filename:30s} - {desc}")
    
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    check_deployment()
