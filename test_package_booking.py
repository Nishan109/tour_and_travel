#!/usr/bin/env python3

print("=== PACKAGE BOOKING STEP-BY-STEP GUIDE ===")
print()

print("📦 WHAT ARE PACKAGES?")
print("Packages combine flights + hotels + tourist attractions in one booking")
print("Perfect for complete travel experiences!")
print()

print("🎯 HOW TO BOOK A PACKAGE:")
print()

print("STEP 1: Go to Package Search")
print("  URL: /package/")
print("  This is the main package search page")
print()

print("STEP 2: Fill Search Form")
print("  Source: MUMBAI")
print("  Destination: DELHI") 
print("  Date: 2026-01-20")
print("  Click 'SEARCH'")
print()

print("STEP 3: Review Package Contents")
print("  You'll see:")
print("  ✈️  Available flights from MUMBAI to DELHI")
print("  🏨  Available hotels in DELHI")
print("  🏛️  Famous places to visit in DELHI")
print("  📦  'Book Package' button at bottom")
print()

print("STEP 4: Book the Package")
print("  Click 'Book Package' button")
print("  Goes to: /bookpackage/MUMBAI/DELHI/2026-01-20")
print("  Select:")
print("    - Flight: DL1425 (INDIGO)")
print("    - Hotel: The Lalit New Delhi")
print("    - Seats: 2")
print("    - Rooms: 1")
print("  Click 'BOOK'")
print()

print("STEP 5: Confirmation")
print("  Package saved to database")
print("  Redirects to dashboard")
print("  Shows in 'Package Bookings' section")
print()

print("🌟 BEST PACKAGE ROUTES TO TRY:")
print()

routes = [
    ("MUMBAI", "DELHI", "3 flights, 5 hotels"),
    ("MUMBAI", "COCHIN", "2 flights, 3 hotels"), 
    ("DELHI", "GOA", "1 flight, 2 hotels"),
    ("MUMBAI", "SRINAGAR", "2 flights, 3 hotels"),
    ("CHANDIGARH", "MUMBAI", "1 flight, 5 hotels")
]

for source, dest, details in routes:
    print(f"  {source} → {dest}: {details}")

print()
print("🎉 TRY IT NOW!")
print("1. Login as 'cleantest' / 'clean123'")
print("2. Go to /package/")
print("3. Search MUMBAI → DELHI")
print("4. Book a complete package!")
print()
print("Your package will include flight + hotel + sightseeing info!")