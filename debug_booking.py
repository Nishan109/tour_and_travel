#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User
from travelapp.models import BookFlight, BookHotel, BookPackage
from datetime import date

print("=== BOOKING DEBUG ===")

# Check all users and their bookings
print("\n📊 All Users and Their Bookings:")
for user in User.objects.all():
    flights = BookFlight.objects.filter(username_id=user)
    hotels = BookHotel.objects.filter(username_id=user)
    packages = BookPackage.objects.filter(username_id=user)
    
    print(f"\n👤 User: {user.username} (ID: {user.id})")
    print(f"   ✈️  Flights: {flights.count()}")
    for flight in flights:
        print(f"      - {flight.flight} on {flight.date} ({flight.seat} seats)")
    
    print(f"   🏨 Hotels: {hotels.count()}")
    for hotel in hotels:
        print(f"      - {hotel.hotel_name} on {hotel.date} ({hotel.room} rooms)")
    
    print(f"   📦 Packages: {packages.count()}")
    for package in packages:
        print(f"      - {package.flight}/{package.hotel_name} on {package.date}")

# Test creating a new booking for a different user
print(f"\n🧪 TESTING NEW BOOKING...")

# Get or create a test user
test_user, created = User.objects.get_or_create(
    username='testbooking',
    defaults={
        'email': 'test@booking.com',
        'first_name': 'Test',
        'last_name': 'Booking'
    }
)

if created:
    test_user.set_password('test123')
    test_user.save()
    print(f"✅ Created test user: testbooking")
else:
    print(f"✅ Using existing test user: testbooking")

# Clear existing bookings for clean test
BookFlight.objects.filter(username_id=test_user).delete()
BookHotel.objects.filter(username_id=test_user).delete()
BookPackage.objects.filter(username_id=test_user).delete()

# Create a test booking
today_str = date.today().strftime('%B %d, %Y')
print(f"📅 Creating booking for date: {today_str}")

try:
    # Create flight booking
    new_booking = BookFlight.objects.create(
        username_id=test_user,
        flight='AI101',
        date=today_str,
        seat=1
    )
    print(f"✅ Created flight booking: {new_booking.flight} for {new_booking.username_id.username}")
    
    # Verify it was saved
    saved_bookings = BookFlight.objects.filter(username_id=test_user)
    print(f"✅ Verified: {saved_bookings.count()} booking(s) found for {test_user.username}")
    
    for booking in saved_bookings:
        print(f"   - Flight: {booking.flight}, Date: {booking.date}, Seats: {booking.seat}")
        
except Exception as e:
    print(f"❌ Error creating booking: {e}")

print(f"\n🔑 Test Login Credentials:")
print(f"Username: testbooking")
print(f"Password: test123")
print(f"\n📝 Instructions:")
print(f"1. Login with testbooking/test123")
print(f"2. Make a new flight booking")
print(f"3. Check if it appears in dashboard")
print(f"4. If not, there's an issue with the booking process")