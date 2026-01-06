# 📦 Package Booking System Guide

## How Packages Work

Packages are **combination deals** that include both **flights + hotels + tourist places** in one booking. They're perfect for complete travel experiences.

## 🎯 Package Booking Workflow

### Step 1: Search for Packages
1. Go to `/package/` 
2. Fill out the search form:
   - **Source**: Where you're traveling from (e.g., MUMBAI)
   - **Destination**: Where you want to go (e.g., DELHI)  
   - **Date**: Travel date (e.g., 2026-01-15)
3. Click **SEARCH**

### Step 2: Review Package Contents
After searching, you'll see:
- **Available Flights** from source to destination
- **Available Hotels** in the destination city
- **Famous Places** to visit in that city
- **"Book Package" button** at the bottom

### Step 3: Book the Package
1. Click **"Book Package"** button
2. You'll go to `/bookpackage/{source}/{city}/{date}`
3. Select your preferences:
   - **Flight**: Choose from available flights
   - **Hotel**: Choose from available hotels  
   - **Seats**: Number of flight seats needed
   - **Rooms**: Number of hotel rooms needed
4. Click **BOOK** to confirm

### Step 4: Confirmation
- Package gets saved to database
- Redirects to your dashboard
- Shows in "Package Bookings" section

## 🧪 Test Package Booking

### Available Routes for Testing:
```
MUMBAI → DELHI (3 flights available)
DELHI → MUMBAI (1 flight available)  
MUMBAI → COCHIN (2 flights available)
CHANDIGARH → DELHI (1 flight available)
DELHI → CHANDIGARH (1 flight available)
```

### Sample Test:
1. **Search**: MUMBAI → DELHI, Date: 2026-01-15
2. **Results**: Will show flights, hotels in Delhi, and Delhi attractions
3. **Book**: Select DL1425 flight + Taj Chandigarh hotel + 2 seats + 1 room
4. **Confirm**: Package booking created

## 🏗️ Technical Details

### What's Included in a Package:
- **Flight booking** (stored in BookPackage.flight)
- **Hotel booking** (stored in BookPackage.hotel_name)  
- **Seat count** (BookPackage.seat)
- **Room count** (BookPackage.room)
- **Travel date** (BookPackage.date)
- **User** (BookPackage.username_id)

### Package vs Individual Bookings:
- **Individual**: Book flight and hotel separately
- **Package**: Book flight + hotel together in one transaction
- **Advantage**: Packages ensure availability of both flight and hotel for same dates

### Database Model:
```python
class BookPackage(models.Model):
    username_id = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.IntegerField(default=1)
    flight = models.CharField(max_length=10)
    hotel_name = models.CharField(max_length=10)  
    room = models.IntegerField(default=1)
    date = models.CharField(max_length=20)
```

## 🎉 Benefits of Package Booking

1. **Convenience**: Book flight + hotel in one go
2. **Availability**: Ensures both are available for same dates
3. **Tourism**: Shows famous places to visit
4. **Coordination**: Single booking for complete trip
5. **Dashboard**: View complete package details in one place

## 🔗 URL Structure

- **Package Search**: `/package/`
- **Package Booking**: `/bookpackage/{source}/{city}/{date}`
- **Package Confirmation**: `/packagesubmit/{flight}/{hotel}/{date}/{seats}/{rooms}`
- **Package Cancellation**: `/cancelpackage/{flight}/{seat}/{hotel}/{date}/{room}`

Try booking a package now! Go to `/package/` and search for MUMBAI → DELHI.