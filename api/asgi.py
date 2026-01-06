import os

# Ensure Django settings are available for the ASGI app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')

from django.core.asgi import get_asgi_application

# Export the ASGI app for Vercel's Python serverless runtime
app = get_asgi_application()