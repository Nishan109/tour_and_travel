#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User
from travelapp.models import BookFlight, BookHotel, BookPackage

print("=== DASHBOARD TEST ===")

# Check admin user bookings
try:
    admin_user = User.objects.get(username='admin')
    flights = BookFlight.objects.filter(username_id=admin_user)
    hotels = BookHotel.objects.filter(username_id=admin_user)
    packages = BookPackage.objects.filter(username_id=admin_user)
    
    print(f"✅ Admin user found: {admin_user.username}")
    print(f"📊 Dashboard data for admin:")
    print(f"   - Flights: {flights.count()}")
    print(f"   - Hotels: {hotels.count()}")
    print(f"   - Packages: {packages.count()}")
    
    if flights.exists():
        print(f"\n✈️  Flight Bookings:")
        for flight in flights:
            print(f"   - {flight.flight} on {flight.date} ({flight.seat} seats)")
    
    if hotels.exists():
        print(f"\n🏨 Hotel Bookings:")
        for hotel in hotels:
            print(f"   - {hotel.hotel_name} on {hotel.date} ({hotel.room} rooms)")
    
    if packages.exists():
        print(f"\n📦 Package Bookings:")
        for package in packages:
            print(f"   - {package.flight}/{package.hotel_name} on {package.date}")
    
    print(f"\n🔑 Login with: admin / admin123")
    print(f"🌐 Then visit: http://127.0.0.1:8000/accounts/profile/")
    
except User.DoesNotExist:
    print("❌ Admin user not found. Run fix_dashboard.py first.")