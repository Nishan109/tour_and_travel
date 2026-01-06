#!/usr/bin/env python
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from django.db import connection
from travelapp.models import City, Flights, Hotels, Famous

print('=== DATABASE TABLES ===')
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    for table in tables:
        print(f'  - {table[0]}')

print('\n=== SAMPLE DATA FROM KEY TABLES ===')

print('\nSample Cities:')
for city in City.objects.all()[:5]:
    print(f'  {city.id}: {city.city}')

print('\nSample Flights:')
for flight in Flights.objects.all()[:5]:
    print(f'  {flight.flight_num}: {flight.source} -> {flight.destination} | ₹{flight.eprice} | {flight.seats} seats')

print('\nSample Hotels:')
for hotel in Hotels.objects.all()[:5]:
    print(f'  {hotel.hotel_name}: {hotel.city.city} | ₹{hotel.hotel_price} | {hotel.rooms} rooms')

print(f'\n=== DATABASE STATISTICS ===')
print(f'Total Cities: {City.objects.count()}')
print(f'Total Flights: {Flights.objects.count()}')
print(f'Total Hotels: {Hotels.objects.count()}')
print(f'Total Famous Places: {Famous.objects.count()}')