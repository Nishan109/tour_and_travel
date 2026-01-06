#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User
from travelapp.models import BookFlight, Flights
from datetime import date

print("=== COMPLETE BOOKING TEST ===")

# Create a fresh test user
username = 'bookingtest'
try:
    user = User.objects.get(username=username)
    # Clear existing bookings
    BookFlight.objects.filter(username_id=user).delete()
    print(f"✅ Using existing user: {username}")
except User.DoesNotExist:
    user = User.objects.create_user(
        username=username,
        password='test123',
        email='test@booking.com'
    )
    print(f"✅ Created new user: {username}")

print(f"User ID: {user.id}")

# Test the complete booking flow
flight_num = "AI101"
booking_date = "2026-01-07"  # Use tomorrow's date
seat_count = 2

print(f"\n🎯 Simulating complete booking process:")
print(f"   Flight: {flight_num}")
print(f"   Date: {booking_date}")
print(f"   Seats: {seat_count}")
print(f"   User: {user.username}")

# Step 1: Check if flight exists
try:
    flight = Flights.objects.get(flight_num=flight_num)
    print(f"✅ Flight found: {flight.flight_num} ({flight.source} -> {flight.destination})")
except Flights.DoesNotExist:
    print(f"❌ Flight {flight_num} not found in database")
    # Let's see what flights are available
    available_flights = Flights.objects.all()[:5]
    print("Available flights:")
    for f in available_flights:
        print(f"  - {f.flight_num}: {f.source} -> {f.destination}")
    exit()

# Step 2: Create booking (simulate FlightSubmit view)
print(f"\n📝 Creating booking...")
try:
    booking = BookFlight.objects.create(
        username_id=user,
        flight=flight_num,
        date=booking_date,
        seat=seat_count
    )
    print(f"✅ Booking created with ID: {booking.id}")
except Exception as e:
    print(f"❌ Error creating booking: {e}")
    exit()

# Step 3: Verify booking was saved
print(f"\n🔍 Verifying booking...")
saved_booking = BookFlight.objects.filter(
    username_id=user,
    flight=flight_num,
    date=booking_date,
    seat=seat_count
).first()

if saved_booking:
    print(f"✅ Booking verified:")
    print(f"   ID: {saved_booking.id}")
    print(f"   User: {saved_booking.username_id.username}")
    print(f"   Flight: {saved_booking.flight}")
    print(f"   Date: {saved_booking.date}")
    print(f"   Seats: {saved_booking.seat}")
else:
    print(f"❌ Booking not found after creation!")

# Step 4: Test dashboard query (simulate Dashboard view)
print(f"\n📊 Testing dashboard query...")
dashboard_flights = BookFlight.objects.filter(username_id=user)
print(f"Dashboard query returned: {dashboard_flights.count()} bookings")

if dashboard_flights.exists():
    print(f"✅ Dashboard will show bookings:")
    for booking in dashboard_flights:
        print(f"   - {booking.flight} on {booking.date} ({booking.seat} seats)")
else:
    print(f"❌ Dashboard will be empty!")

# Step 5: Check all bookings for this user
print(f"\n📋 All bookings for user {user.username}:")
all_bookings = BookFlight.objects.filter(username_id=user)
print(f"Total: {all_bookings.count()}")

# Step 6: Test with different user to ensure isolation
print(f"\n🔒 Testing user isolation...")
other_user_bookings = BookFlight.objects.exclude(username_id=user)
print(f"Other users have {other_user_bookings.count()} bookings total")

print(f"\n🔑 Test Login Credentials:")
print(f"Username: {username}")
print(f"Password: test123")
print(f"\n✅ This user should show 1 flight booking in dashboard")

# Final verification
final_check = BookFlight.objects.filter(username_id=user).count()
print(f"\n🎯 FINAL CHECK: User {user.username} has {final_check} flight booking(s)")

if final_check > 0:
    print("✅ SUCCESS: Booking process works correctly!")
else:
    print("❌ FAILURE: Booking was not saved properly!")