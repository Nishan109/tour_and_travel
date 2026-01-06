#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User
from travelapp.models import BookFlight, Flights
from datetime import date

print("=== TESTING BOOKING FLOW ===")

# Get the testbooking user
try:
    user = User.objects.get(username='testbooking')
    print(f"✅ Found user: {user.username}")
except User.DoesNotExist:
    print("❌ User 'testbooking' not found. Run debug_booking.py first.")
    exit()

# Clear existing bookings
BookFlight.objects.filter(username_id=user).delete()
print("🧹 Cleared existing bookings")

# Test different date formats
test_dates = [
    "2026-01-06",  # YYYY-MM-DD format (from form)
    "January 06, 2026",  # Full format (stored format)
    "Jan. 6, 2026",  # Short format
]

flight_num = "AI101"
seat_count = 1

print(f"\n🧪 Testing booking with different date formats:")

for i, test_date in enumerate(test_dates):
    print(f"\n📅 Test {i+1}: Date format '{test_date}'")
    
    try:
        # Simulate the FlightSubmit view
        booking = BookFlight(
            username_id=user,
            flight=flight_num,
            date=test_date,
            seat=seat_count
        )
        booking.save()
        print(f"✅ Booking saved successfully")
        
        # Verify it was saved
        saved_booking = BookFlight.objects.filter(
            username_id=user,
            flight=flight_num,
            date=test_date
        ).first()
        
        if saved_booking:
            print(f"✅ Booking verified in database")
            print(f"   - Flight: {saved_booking.flight}")
            print(f"   - Date: {saved_booking.date}")
            print(f"   - Seats: {saved_booking.seat}")
            print(f"   - User: {saved_booking.username_id.username}")
        else:
            print(f"❌ Booking not found in database")
            
    except Exception as e:
        print(f"❌ Error saving booking: {e}")

# Check all bookings for this user
print(f"\n📊 All bookings for {user.username}:")
all_bookings = BookFlight.objects.filter(username_id=user)
print(f"Total bookings: {all_bookings.count()}")

for booking in all_bookings:
    print(f"  - {booking.flight} on {booking.date} ({booking.seat} seats)")

# Test the dashboard query
print(f"\n🎯 Testing Dashboard Query:")
dashboard_bookings = BookFlight.objects.filter(username_id=user)
print(f"Dashboard would show: {dashboard_bookings.count()} flight bookings")

if dashboard_bookings.exists():
    print("✅ Dashboard should show bookings")
else:
    print("❌ Dashboard will be empty")

print(f"\n🔍 Debugging Info:")
print(f"User ID: {user.id}")
print(f"User object: {user}")
print(f"Username: {user.username}")

# Check if there are any bookings with similar flight numbers
similar_bookings = BookFlight.objects.filter(flight__icontains="AI101")
print(f"\nSimilar flight bookings in database: {similar_bookings.count()}")
for booking in similar_bookings:
    print(f"  - {booking.flight} by {booking.username_id.username} on {booking.date}")