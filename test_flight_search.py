#!/usr/bin/env python3

import os
import django
import sys

# Add the project directory to Python path
sys.path.append('/path/to/your/project')

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from travelapp.models import Flights
from datetime import datetime

print("=== FLIGHT SEARCH TEST ===")
print("\nAvailable flight routes:")

# Group flights by route
routes = {}
for flight in Flights.objects.all():
    route = f"{flight.source} -> {flight.destination}"
    if route not in routes:
        routes[route] = []
    routes[route].append(flight)

for route, flights in routes.items():
    print(f"\n{route}:")
    for flight in flights:
        print(f"  {flight.flight_num} ({flight.company}) - ₹{flight.eprice}")

print("\n=== SEARCH EXAMPLE ===")
print("To search for flights:")
print("1. Go to /flights/")
print("2. Enter Source: MUMBAI")
print("3. Enter Destination: DELHI") 
print("4. Enter Date: 2026-01-10")
print("5. Click SEARCH")
print("6. Click on any flight result to book")

# Test a specific search
print("\n=== TESTING MUMBAI -> DELHI SEARCH ===")
mumbai_delhi_flights = Flights.objects.filter(source='MUMBAI', destination='DELHI')
print(f"Found {mumbai_delhi_flights.count()} flights:")
for flight in mumbai_delhi_flights:
    print(f"  {flight.flight_num}: {flight.company} - ₹{flight.eprice}")
    print(f"    Departure: {flight.dept_time}, Arrival: {flight.dest_time}")
    print(f"    Available seats: {flight.seats}")