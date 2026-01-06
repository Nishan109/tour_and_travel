#!/usr/bin/env python
import os
import sys
import django
from datetime import time

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourAndTravel.settings')
django.setup()

from travelapp.models import City, Flights, Hotels, Famous

def populate_data():
    print("Adding sample data...")
    
    # Create Cities
    cities_data = [
        {'city': 'DELHI', 'bestlink': 'https://example.com/delhi', 'weekgetlinks': 'https://example.com/delhi-week'},
        {'city': 'MUMBAI', 'bestlink': 'https://example.com/mumbai', 'weekgetlinks': 'https://example.com/mumbai-week'},
        {'city': 'CHANDIGARH', 'bestlink': 'https://example.com/chandigarh', 'weekgetlinks': 'https://example.com/chandigarh-week'},
        {'city': 'GOA', 'bestlink': 'https://example.com/goa', 'weekgetlinks': 'https://example.com/goa-week'},
        {'city': 'BANGALORE', 'bestlink': 'https://example.com/bangalore', 'weekgetlinks': 'https://example.com/bangalore-week'},
    ]
    
    for city_data in cities_data:
        city, created = City.objects.get_or_create(
            city=city_data['city'],
            defaults={
                'bestlink': city_data['bestlink'],
                'weekgetlinks': city_data['weekgetlinks']
            }
        )
        if created:
            print(f"Created city: {city.city}")
    
    # Create Flights
    flights_data = [
        {'source': 'CHANDIGARH', 'destination': 'DELHI', 'flight_num': 'AI101', 'city': 'DELHI', 'eprice': 5000, 'dept_time': time(8, 0), 'dest_time': time(9, 30), 'company': 'Air India', 'seats': 150},
        {'source': 'DELHI', 'destination': 'CHANDIGARH', 'flight_num': 'AI102', 'city': 'CHANDIGARH', 'eprice': 5200, 'dept_time': time(14, 0), 'dest_time': time(15, 30), 'company': 'Air India', 'seats': 150},
        {'source': 'CHANDIGARH', 'destination': 'MUMBAI', 'flight_num': 'SG201', 'city': 'MUMBAI', 'eprice': 8000, 'dept_time': time(10, 0), 'dest_time': time(12, 30), 'company': 'SpiceJet', 'seats': 180},
        {'source': 'MUMBAI', 'destination': 'CHANDIGARH', 'flight_num': 'SG202', 'city': 'CHANDIGARH', 'eprice': 8200, 'dept_time': time(16, 0), 'dest_time': time(18, 30), 'company': 'SpiceJet', 'seats': 180},
        {'source': 'DELHI', 'destination': 'GOA', 'flight_num': 'IG301', 'city': 'GOA', 'eprice': 12000, 'dept_time': time(7, 0), 'dest_time': time(9, 45), 'company': 'IndiGo', 'seats': 200},
        {'source': 'GOA', 'destination': 'DELHI', 'flight_num': 'IG302', 'city': 'DELHI', 'eprice': 12500, 'dept_time': time(18, 0), 'dest_time': time(20, 45), 'company': 'IndiGo', 'seats': 200},
    ]
    
    for flight_data in flights_data:
        try:
            city_obj = City.objects.get(city=flight_data['city'])
            flight, created = Flights.objects.get_or_create(
                flight_num=flight_data['flight_num'],
                defaults={
                    'source': flight_data['source'],
                    'destination': flight_data['destination'],
                    'city': city_obj,
                    'eprice': flight_data['eprice'],
                    'dept_time': flight_data['dept_time'],
                    'dest_time': flight_data['dest_time'],
                    'company': flight_data['company'],
                    'seats': flight_data['seats']
                }
            )
            if created:
                print(f"Created flight: {flight.flight_num}")
        except City.DoesNotExist:
            print(f"City {flight_data['city']} not found for flight {flight_data['flight_num']}")
    
    # Create Hotels
    hotels_data = [
        {'city': 'DELHI', 'hotel_name': 'Taj Palace', 'hotel_address': 'Diplomatic Enclave, New Delhi', 'hotel_price': 8000, 'hotel_rating': 5, 'amenities': 'WiFi, Pool, Spa, Restaurant', 'distfromap': 15, 'rooms': 50},
        {'city': 'DELHI', 'hotel_name': 'Hotel Metropolis', 'hotel_address': 'Karol Bagh, New Delhi', 'hotel_price': 4000, 'hotel_rating': 4, 'amenities': 'WiFi, Restaurant, AC', 'distfromap': 10, 'rooms': 30},
        {'city': 'MUMBAI', 'hotel_name': 'The Oberoi', 'hotel_address': 'Nariman Point, Mumbai', 'hotel_price': 12000, 'hotel_rating': 5, 'amenities': 'WiFi, Pool, Spa, Restaurant, Bar', 'distfromap': 5, 'rooms': 40},
        {'city': 'MUMBAI', 'hotel_name': 'Hotel Marine Plaza', 'hotel_address': 'Marine Drive, Mumbai', 'hotel_price': 6000, 'hotel_rating': 4, 'amenities': 'WiFi, Restaurant, Sea View', 'distfromap': 2, 'rooms': 35},
        {'city': 'CHANDIGARH', 'hotel_name': 'Taj Chandigarh', 'hotel_address': 'Block No 9, Sector 17A, Chandigarh', 'hotel_price': 7000, 'hotel_rating': 5, 'amenities': 'WiFi, Pool, Spa, Restaurant', 'distfromap': 8, 'rooms': 45},
        {'city': 'CHANDIGARH', 'hotel_name': 'Hotel Sunbeam', 'hotel_address': 'Sector 22, Chandigarh', 'hotel_price': 3500, 'hotel_rating': 3, 'amenities': 'WiFi, Restaurant, AC', 'distfromap': 12, 'rooms': 25},
        {'city': 'GOA', 'hotel_name': 'Taj Exotica', 'hotel_address': 'Benaulim, South Goa', 'hotel_price': 15000, 'hotel_rating': 5, 'amenities': 'Beach Access, Pool, Spa, Restaurant', 'distfromap': 20, 'rooms': 60},
        {'city': 'GOA', 'hotel_name': 'Hotel Fidalgo', 'hotel_address': 'Panaji, North Goa', 'hotel_price': 5000, 'hotel_rating': 4, 'amenities': 'WiFi, Pool, Restaurant', 'distfromap': 5, 'rooms': 30},
    ]
    
    for hotel_data in hotels_data:
        try:
            city_obj = City.objects.get(city=hotel_data['city'])
            hotel, created = Hotels.objects.get_or_create(
                hotel_name=hotel_data['hotel_name'],
                defaults={
                    'city': city_obj,
                    'hotel_address': hotel_data['hotel_address'],
                    'hotel_price': hotel_data['hotel_price'],
                    'hotel_rating': hotel_data['hotel_rating'],
                    'amenities': hotel_data['amenities'],
                    'distfromap': hotel_data['distfromap'],
                    'rooms': hotel_data['rooms']
                }
            )
            if created:
                print(f"Created hotel: {hotel.hotel_name}")
        except City.DoesNotExist:
            print(f"City {hotel_data['city']} not found for hotel {hotel_data['hotel_name']}")
    
    # Create Famous Places
    famous_places_data = [
        {'city': 'DELHI', 'place_name': 'Red Fort', 'desc': 'Historic fortified palace of the Mughal emperors'},
        {'city': 'DELHI', 'place_name': 'India Gate', 'desc': 'War memorial arch in New Delhi'},
        {'city': 'DELHI', 'place_name': 'Qutub Minar', 'desc': 'Tallest brick minaret in the world'},
        {'city': 'MUMBAI', 'place_name': 'Gateway of India', 'desc': 'Iconic arch monument overlooking the Arabian Sea'},
        {'city': 'MUMBAI', 'place_name': 'Marine Drive', 'desc': 'Beautiful waterfront promenade'},
        {'city': 'MUMBAI', 'place_name': 'Elephanta Caves', 'desc': 'Ancient rock-cut caves dedicated to Lord Shiva'},
        {'city': 'CHANDIGARH', 'place_name': 'Rock Garden', 'desc': 'Unique sculpture garden made from recycled materials'},
        {'city': 'CHANDIGARH', 'place_name': 'Sukhna Lake', 'desc': 'Artificial lake perfect for boating and relaxation'},
        {'city': 'CHANDIGARH', 'place_name': 'Rose Garden', 'desc': 'Beautiful botanical garden with thousands of rose varieties'},
        {'city': 'GOA', 'place_name': 'Baga Beach', 'desc': 'Popular beach known for water sports and nightlife'},
        {'city': 'GOA', 'place_name': 'Basilica of Bom Jesus', 'desc': 'UNESCO World Heritage Site church'},
        {'city': 'GOA', 'place_name': 'Dudhsagar Falls', 'desc': 'Spectacular four-tiered waterfall'},
    ]
    
    for place_data in famous_places_data:
        try:
            city_obj = City.objects.get(city=place_data['city'])
            place, created = Famous.objects.get_or_create(
                place_name=place_data['place_name'],
                city=city_obj,
                defaults={
                    'desc': place_data['desc']
                }
            )
            if created:
                print(f"Created famous place: {place.place_name}")
        except City.DoesNotExist:
            print(f"City {place_data['city']} not found for place {place_data['place_name']}")
    
    print("Sample data population completed!")

if __name__ == '__main__':
    populate_data()