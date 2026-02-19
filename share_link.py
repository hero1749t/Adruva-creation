#!/usr/bin/env python
"""Generate ngrok public URL for sharing Django app with friends."""

import time
from pyngrok import ngrok
from urllib.parse import urlparse

# Configure ngrok to use HTTPS
ngrok.set_auth_token("2sMNIDVlNUTx1P8oDvPsJJVWZKG_4dFr6M7b5R5MZT7d7zx28")  # Free auth token

# Create tunnel to localhost:8000
tunnel = ngrok.connect(8000, "http")
public_url = tunnel.public_url

print("\n" + "="*70)
print("🎉 YOUR WEBSITE IS NOW PUBLICLY ACCESSIBLE!")
print("="*70)
print(f"\n📱 Share this link with your friend:\n")
print(f"  ✨ {public_url}\n")
print("="*70)
print("\nℹ️  Notes:")
print("  • This link is valid for a few hours (free ngrok)")
print("  • Your friend can open it directly in browser")
print("  • No need to visit GitHub!")
print("  • Server must keep running")
print("\n" + "="*70 + "\n")

# Keep tunnel alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n✋ Tunnel closed!")
    ngrok.disconnect(public_url)
