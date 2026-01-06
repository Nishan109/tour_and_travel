#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User
from travelapp.models import BookFlight, BookHotel, BookPackage
from datetime import date

# Create a test user
username = 'testuser'
password = 'testpass123'

# Check if user exists, if not create one
user, created = User.objects.get_or_create(
    username=username,
    defaults={
        'email': 'test@example.com',
        'first_name': 'Test',
        'last_name': 'User'
    }
)

if created:
    user.set_password(password)
    user.save()
    print(f"Created new user: {username}")
else:
    print(f"User {username} already exists")

# Create some test bookings for this user
today = date.today().strftime('%B %d, %Y')

# Create flight booking
flight_booking = BookFlight.objects.create(
    username_id=user,
    flight='AI101',
    date=today,
    seat=2
)

# Create hotel booking
hotel_booking = BookHotel.objects.create(
    username_id=user,
    hotel_name='Taj Palace',
    date=today,
    room=1
)

# Create package booking
package_booking = BookPackage.objects.create(
    username_id=user,
    flight='IG301',
    hotel_name='Hotel Fidalgo',
    date=today,
    seat=2,
    room=1
)

print(f"Created test bookings for user {username}:")
print(f"- Flight: {flight_booking.flight} on {flight_booking.date}")
print(f"- Hotel: {hotel_booking.hotel_name} on {hotel_booking.date}")
print(f"- Package: {package_booking.flight}/{package_booking.hotel_name} on {package_booking.date}")
print(f"\nLogin credentials:")
print(f"Username: {username}")
print(f"Password: {password}")