#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.contrib.auth.models import User
from travelapp.models import BookFlight, BookHotel, BookPackage
from datetime import date

print("=== DASHBOARD DEBUG & FIX ===")

# Show all users
print("\nAll Users in Database:")
for user in User.objects.all():
    flight_count = BookFlight.objects.filter(username_id=user).count()
    hotel_count = BookHotel.objects.filter(username_id=user).count()
    package_count = BookPackage.objects.filter(username_id=user).count()
    print(f"  {user.username} (ID: {user.id}) - Flights: {flight_count}, Hotels: {hotel_count}, Packages: {package_count}")

# Create a superuser for testing if it doesn't exist
admin_user, created = User.objects.get_or_create(
    username='admin',
    defaults={
        'email': 'admin@example.com',
        'first_name': 'Admin',
        'last_name': 'User',
        'is_staff': True,
        'is_superuser': True
    }
)

if created:
    admin_user.set_password('admin123')
    admin_user.save()
    print(f"\nCreated admin user: admin / admin123")
else:
    print(f"\nAdmin user already exists")

# Add sample bookings for admin user
today = date.today().strftime('%B %d, %Y')

# Clear existing bookings for admin to avoid duplicates
BookFlight.objects.filter(username_id=admin_user).delete()
BookHotel.objects.filter(username_id=admin_user).delete()
BookPackage.objects.filter(username_id=admin_user).delete()

# Create new bookings
flight1 = BookFlight.objects.create(
    username_id=admin_user,
    flight='AI101',
    date=today,
    seat=2
)

flight2 = BookFlight.objects.create(
    username_id=admin_user,
    flight='IG301',
    date='January 15, 2026',
    seat=1
)

hotel1 = BookHotel.objects.create(
    username_id=admin_user,
    hotel_name='Taj Palace',
    date=today,
    room=1
)

hotel2 = BookHotel.objects.create(
    username_id=admin_user,
    hotel_name='The Oberoi',
    date='January 10, 2026',
    room=2
)

package1 = BookPackage.objects.create(
    username_id=admin_user,
    flight='SG201',
    hotel_name='Hotel Fidalgo',
    date='January 20, 2026',
    seat=2,
    room=1
)

print(f"\nCreated sample bookings for admin user:")
print(f"✅ Flight Bookings: {BookFlight.objects.filter(username_id=admin_user).count()}")
print(f"✅ Hotel Bookings: {BookHotel.objects.filter(username_id=admin_user).count()}")
print(f"✅ Package Bookings: {BookPackage.objects.filter(username_id=admin_user).count()}")

print(f"\n🔑 LOGIN CREDENTIALS:")
print(f"Username: admin")
print(f"Password: admin123")
print(f"\n📋 After logging in with these credentials, your dashboard will show:")
print(f"   - 2 Flight bookings")
print(f"   - 2 Hotel bookings") 
print(f"   - 1 Package booking")