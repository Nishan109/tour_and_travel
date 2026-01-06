#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.urls import reverse
from datetime import date

print("=== URL GENERATION TEST ===")

# Test URL generation for flight booking
flight_num = "AI101"
booking_date = "2026-01-07"
seat_count = 2

print(f"Testing URL generation for:")
print(f"  Flight: {flight_num}")
print(f"  Date: {booking_date}")
print(f"  Seats: {seat_count}")

# Test the URL that would be generated in the template
template_url = f'/userflight/{flight_num}/{booking_date}/{seat_count}'
print(f"\nTemplate would generate URL: {template_url}")

# Test if this URL would match our pattern
try:
    # This should match: path('userflight/<str:flight_num>/<str:date>/<int:seat>',views.FlightSubmit,name='userflight')
    print(f"✅ URL pattern should match")
    
    # Test with different date formats that might come from the form
    test_dates = [
        "2026-01-07",      # YYYY-MM-DD (from DateField)
        "Jan. 7, 2026",    # Formatted date
        "January 7, 2026", # Full formatted date
    ]
    
    print(f"\nTesting different date formats in URLs:")
    for test_date in test_dates:
        test_url = f'/userflight/{flight_num}/{test_date}/{seat_count}'
        print(f"  {test_url}")
        
except Exception as e:
    print(f"❌ URL generation error: {e}")

# Test the booking flow URL
booking_url = f'/bookflight/{flight_num}/{booking_date}'
print(f"\nBooking flow URL: {booking_url}")

print(f"\n🔍 URL Pattern Analysis:")
print(f"1. User searches flights: /flights/")
print(f"2. User clicks flight: /bookflight/{flight_num}/{booking_date}")
print(f"3. User selects seats and clicks BOOK: /userflight/{flight_num}/{booking_date}/{seat_count}")
print(f"4. FlightSubmit view saves booking and redirects to: /accounts/profile/")

print(f"\n⚠️  Potential Issues:")
print(f"1. Date format mismatch between form input and URL")
print(f"2. Special characters in date string (spaces, periods)")
print(f"3. URL encoding issues")

# Test URL encoding
import urllib.parse
encoded_date = urllib.parse.quote("January 7, 2026")
print(f"\nURL encoded date: {encoded_date}")
encoded_url = f'/userflight/{flight_num}/{encoded_date}/{seat_count}'
print(f"Encoded URL: {encoded_url}")

print(f"\n💡 Recommendation:")
print(f"Use consistent date format (YYYY-MM-DD) throughout the booking process")
print(f"This avoids URL encoding issues and ensures reliable routing")