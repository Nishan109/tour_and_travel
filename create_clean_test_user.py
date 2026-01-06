#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User
from travelapp.models import BookFlight, BookHotel, BookPackage
from datetime import date

print("=== CREATING CLEAN TEST USER ===")

# Create a completely fresh user for testing
username = 'cleantest'
password = 'clean123'

# Remove user if exists
try:
    existing_user = User.objects.get(username=username)
    BookFlight.objects.filter(username_id=existing_user).delete()
    BookHotel.objects.filter(username_id=existing_user).delete()
    BookPackage.objects.filter(username_id=existing_user).delete()
    existing_user.delete()
    print(f"🧹 Removed existing user and bookings")
except User.DoesNotExist:
    pass

# Create fresh user
user = User.objects.create_user(
    username=username,
    password=password,
    email='clean@test.com',
    first_name='Clean',
    last_name='Test'
)

print(f"✅ Created fresh user: {username}")
print(f"   ID: {user.id}")
print(f"   Email: {user.email}")

# Verify no bookings exist
flights = BookFlight.objects.filter(username_id=user).count()
hotels = BookHotel.objects.filter(username_id=user).count()
packages = BookPackage.objects.filter(username_id=user).count()

print(f"\n📊 Initial booking counts:")
print(f"   Flights: {flights}")
print(f"   Hotels: {hotels}")
print(f"   Packages: {packages}")

if flights == 0 and hotels == 0 and packages == 0:
    print("✅ User has clean slate - no existing bookings")
else:
    print("❌ User has existing bookings - something went wrong")

print(f"\n🔑 LOGIN CREDENTIALS:")
print(f"Username: {username}")
print(f"Password: {password}")

print(f"\n📝 TESTING INSTRUCTIONS:")
print(f"1. Login with the credentials above")
print(f"2. Go to Flights section")
print(f"3. Search for flights (e.g., CHANDIGARH to DELHI)")
print(f"4. Click on a flight to book")
print(f"5. Select number of seats and click BOOK")
print(f"6. Check your dashboard - the booking should appear")
print(f"7. If it doesn't appear, check the server console for DEBUG messages")

print(f"\n🎯 EXPECTED RESULT:")
print(f"After booking, the dashboard should show your new booking")
print(f"The debug messages will help identify any issues in the booking process")