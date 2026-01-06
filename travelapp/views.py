from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignUpForm,HotelForm,FlightForm,ChoiceForm,SeatForm,RoomForm,CityForm
from .models import Flights,Hotels,Famous,BookFlight,BookHotel,BookPackage,City

# Create your views here.

def IndexView(request):
    # Provide quick search forms on the landing page
    return render(request, 'index.html', {
        'flight_form': FlightForm(),
        'hotel_form': HotelForm(),
    })

def custom_logout(request):
    """Custom logout view that handles both GET and POST requests"""
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def PackageView(request):
    form = FlightForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            source = form.cleaned_data['source'].upper()
            date = form.cleaned_data['date']
            destination = form.cleaned_data['destination'].upper()
            # city = destination
            flights = Flights.objects.filter(source=source).filter(destination=destination)
            famplace = Famous.objects.filter(city__city__contains=destination)
            hotels = Hotels.objects.filter(city__city__contains=destination)
            j = hotels[0].city
            s = {'source':source}
            c = {'city':j}
            f = {'Flights':flights}
            d = {'date':date}
            h = {'Hotels':hotels}
            fp = {'Famplace':famplace}
            form = {'form': form}
            form1 = {'form1':form}
            response = {**f,**s,**h,**fp,**form,**d,**c}
            return render(request,'package.html',response)
    else:
        return render(request,'package.html',{'form': form})


def registerView(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
            form=SignUpForm()
    return render(request,'registration/register.html',{'form': form})

def HotelView(request):
    form = HotelForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            city = form.cleaned_data['city'].upper()
            date = form.cleaned_data['date']
            hotels = Hotels.objects.filter(city__city__contains=city)
            d = {'date':date}
            h = {'Hotels':hotels}
            form = {'form': form}
            response = {**h,**d,**form}
            return render(request,'hotels.html',response)
        else:
            return render(request,'hotels.html',{'form': form})

    else:
        return render(request,'hotels.html',{'form': form})

def FlightView(request):
    form = FlightForm(request.POST)
    c = 0;
    if request.method=="POST":
        if form.is_valid():
            source = form.cleaned_data['source'].upper()
            destination = form.cleaned_data['destination'].upper()
            date = form.cleaned_data['date']
            flights = Flights.objects.filter(source=source).filter(destination=destination)
            d = {'date':date}
            f = {'Flights':flights}
            form = {'form': form}
            response = {**f,**d,**form}
            return render(request,'flights.html',response)
        else:
            return render(request,'flights.html',{'form': form})
    else:
        return render(request,'flights.html',{'form': form})

@login_required
def Dashboard(request):
    user = request.user
    print(f"=== DASHBOARD DEBUG ===")
    print(f"User: {user.username} (ID: {user.id})")
    
    f1 = BookFlight.objects.filter(username_id=user)
    h1 = BookHotel.objects.filter(username_id=user)
    p1 = BookPackage.objects.filter(username_id=user)
    
    print(f"Flight bookings found: {f1.count()}")
    print(f"Hotel bookings found: {h1.count()}")
    print(f"Package bookings found: {p1.count()}")
    
    for flight in f1:
        print(f"  Flight: {flight.flight} on {flight.date} ({flight.seat} seats)")
    
    # Check if there are ANY bookings for this user in the database
    all_user_flights = BookFlight.objects.filter(username_id=user)
    print(f"Total flight bookings in DB for {user.username}: {all_user_flights.count()}")
    
    print(f"=== END DASHBOARD DEBUG ===")
    
    f={'flights':f1}
    h={'hotels':h1}
    p={'packages':p1}
    response= {**f,**h,**p}
    return render(request,'dashboard.html',response)

@login_required
def Flightbook(request,flight_num=None,date=None):
    cs=0
    c = None
    price = 0;
    form = SeatForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            flight = Flights.objects.filter(flight_num=flight_num)
            seats = form.cleaned_data['seats']
            # d1=datetime.datetime.strptime(date, "%Y-%m-%d").date()
            for i in flight:
                c = BookFlight.objects.filter(flight=i.flight_num).filter(date=date)
                d = BookPackage.objects.filter(flight=i.flight_num).filter(date=date)
                price = seats*i.eprice
                seatrem = i.seats
            for j in c:
                cs = cs + j.seat
            for k in d:
                cs = cs + k.seat
            seatrem = seatrem - cs
            if (seatrem-seats) > 0:
                avail = "available"
            else:
                avail = "unavailable"
            a = {'availability':avail}
            p = {'price':price}
            sb = {'seatsreq':seats}
            s = {'seatrem':seatrem}
            b = {'flight':flight}
            f = {'form':form}
            d = {'date':date}
            response = {**b,**d,**f,**s,**a,**sb,**p}
            print(s)
            return render(request,'bookflight.html',response)
        else:
            return render(request,'bookflight.html',{'form':form})
    else:
        return render(request,'bookflight.html',{'form':form})

@login_required
def FlightSubmit(request,flight_num=None,date=None,seat=None):
    user = request.user
    
    # Add comprehensive debugging
    print(f"=== FLIGHT BOOKING DEBUG ===")
    print(f"User: {user.username} (ID: {user.id})")
    print(f"Flight: {flight_num}")
    print(f"Date: {date}")
    print(f"Seats: {seat}")
    print(f"Request method: {request.method}")
    
    # Standardize date format to avoid issues
    from datetime import datetime
    try:
        # Try to parse the date and convert to standard format
        if date:
            # Handle different date formats
            try:
                # Try YYYY-MM-DD format first
                parsed_date = datetime.strptime(date, '%Y-%m-%d')
                standardized_date = parsed_date.strftime('%B %d, %Y')
                print(f"Date converted from '{date}' to '{standardized_date}'")
            except ValueError:
                # If that fails, use the date as-is
                standardized_date = date
                print(f"Date used as-is: '{standardized_date}'")
        else:
            standardized_date = date
            print(f"No date provided")
    except Exception as e:
        standardized_date = date
        print(f"Date parsing error: {e}")
    
    try:
        print(f"Creating BookFlight object...")
        b = BookFlight(username_id=user,flight=flight_num,date=standardized_date,seat=seat)
        print(f"BookFlight object created: {b}")
        
        print(f"Saving to database...")
        b.save()
        print(f"Booking saved successfully with ID: {b.id}")
        
        # Verify the booking was saved
        verification = BookFlight.objects.filter(username_id=user, flight=flight_num, date=standardized_date, seat=seat).first()
        if verification:
            # Using ASCII-only logging to avoid encoding issues on some consoles
            print(f"[OK] Booking verified in database: ID {verification.id}")
        else:
            print("[WARN] Booking NOT found in database after save!")
            
        # Check total bookings for this user
        total_bookings = BookFlight.objects.filter(username_id=user).count()
        print(f"Total bookings for {user.username}: {total_bookings}")
        
    except Exception as e:
        print(f"[ERROR] Error saving booking: {e}")
        import traceback
        traceback.print_exc()
    
    print(f"=== END DEBUG ===")
    return redirect('dashboard')

@login_required
def Hotelbook(request,hotel=None,date=None):
    cs=0
    c = None
    price = 0;
    form = RoomForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            room = form.cleaned_data['rooms']
            hotel = Hotels.objects.filter(hotel_name=hotel)
            # d1=datetime.datetime.strptime(date, "%Y-%m-%d").date()
            for i in hotel:
                c1 = BookHotel.objects.filter(hotel_name=i.hotel_name).filter(date=date)
                d1 = BookPackage.objects.filter(hotel_name=i.hotel_name).filter(date=date)
                price = room*i.hotel_price
                roomrem = i.rooms
            for j in c1:
                cs = cs + j.room
            for k in d1:
                cs = cs + k.room
            roomrem = roomrem - cs
            if (roomrem-room) > 0:
                avail = "available"
            else:
                avail = "unavailable"
            a = {'availability':avail}
            p = {'price':price}
            rb = {'roomreq':room}
            r = {'roomrem':roomrem}
            b = {'hotel':hotel}
            f = {'form':form}
            d = {'date':date}
            response = {**b,**d,**a,**p,**rb,**f,**r}
            return render(request,'bookhotel.html',response)
        else:
            return render(request,'bookhotel.html',{'form':form})
    else:
        return render(request,'bookhotel.html',{'form':form})

@login_required
def HotelSubmit(request,hotel=None,date=None,room=None):
    user = request.user
    b = BookHotel(username_id=user,hotel_name=hotel,date=date,room=room)
    b.save()
    return redirect('dashboard')

@login_required
def PackageBook(request,source,city,date):
    c = None
    d = None
    c1 = None
    d1 = None
    roomrem=0
    price1=0
    price=0
    seatrem=0
    cs = 0;
    cs1 = 0;
    form = ChoiceForm(request.POST)
    allf = Flights.objects.filter(source=source).filter(destination=city)
    allh = Hotels.objects.filter(city__city__contains=city)
    af = {'allflights':allf}
    ah={'allhotels':allh}
    form1 = {'form': form}
    if request.method=="POST":
        if form.is_valid():
            flight = form.cleaned_data.get('flight', '').upper()
            hotel = form.cleaned_data.get('hotel', '')
            seats = form.cleaned_data.get('seats', 0) or 0
            room = form.cleaned_data.get('rooms', 0) or 0
            flights = Flights.objects.filter(flight_num=flight)
            hotels = Hotels.objects.filter(hotel_name=hotel)
            
            # Process flight availability
            if flights.exists():
                for i in flights:
                    c = BookFlight.objects.filter(flight=i.flight_num).filter(date=date)
                    d = BookPackage.objects.filter(flight=i.flight_num).filter(date=date)
                    if seats and seats > 0:
                        price = seats*i.eprice
                    seatrem = i.seats
                if c:
                    for j in c:
                        cs = cs + j.seat
                if d:
                    for k in d:
                        cs = cs + k.seat
                seatrem = seatrem - cs
                if seats and seatrem and (seatrem-seats) > 0:
                    availf = "available"
                else:
                    availf = "unavailable"
            else:
                availf = "unavailable"

            # Process hotel availability
            if hotels.exists():
                for l in hotels:
                    c1 = BookHotel.objects.filter(hotel_name=l.hotel_name).filter(date=date)
                    d1 = BookPackage.objects.filter(hotel_name=l.hotel_name).filter(date=date)
                    if room and room > 0:
                        price1 = room*l.hotel_price
                    roomrem = l.rooms
                if c1:
                    for m in c1:
                        cs1 = cs1 + m.room
                if d1:
                    for n in d1:
                        cs1 = cs1 + n.room
                roomrem = roomrem - cs1
                if room and roomrem and (roomrem-room) > 0:
                    availh = "available"
                else:
                    availh = "unavailable"
            else:
                availh = "unavailable"

            a = {'flavailability':availf}
            p = {'pricef':price}
            sb = {'seatsreq':seats}
            s = {'seatrem':seatrem}
            a1 = {'havailability':availh}
            p1 = {'priceh':price1}
            rb = {'roomreq':room}
            r = {'roomrem':roomrem}
            f = {'Flights':flights}
            h = {'Hotels':hotels}
            d = {'date':date}
            response = {**f,**af,**ah,**h,**d,**form1,**a,**a1,**p,**p1,**s,**sb,**r,**rb}
            return render(request,'bookpackage.html',response)
        else:
            response = {**af,**ah,**form1}
            return render(request,'bookhotel.html',response)
    else:
        response = {**af,**ah,**form1}
        return render(request,'bookpackage.html',response)

@login_required
def PackageSubmit(request,flight=None,hotel=None,date=None,seat=None,room=None):
    user = request.user
    b = BookPackage(username_id=user,flight=flight,seat=seat,hotel_name=hotel,room=room,date=date)
    b.save()
    return redirect('dashboard')

@login_required
def CancelFlight(request,flight=None,date=None,seat=None):
    price = 0;
    flight = Flights.objects.filter(flight_num=flight)
    for i in flight:
        price = seat*i.eprice
    f = {'Flight':flight}
    p = {'price':price}
    s = {'seat':seat}
    d = {'date':date}
    response = {**f,**p,**s,**d}
    return render(request,'cancelflight.html',response)

@login_required
def ConfirmCancelFlight(request,flight=None,date=None,seat=None):
    user = request.user
    flight = BookFlight.objects.filter(username_id=user).filter(flight=flight).filter(date=date).filter(seat=seat)
    flight.delete()
    return redirect('dashboard')

@login_required
def CancelHotel(request,hotel=None,date=None,room=None):
    hotel = Hotels.objects.filter(hotel_name=hotel)
    for i in hotel:
        price = room*i.hotel_price
    h = {'Hotel':hotel}
    p = {'price':price}
    r = {'room':room}
    d = {'date':date}
    response = {**h,**p,**r,**d}
    return render(request,'cancelhotel.html',response)

@login_required
def ConfirmCancelHotel(request,hotel=None,date=None,room=None):
    user = request.user
    hotel = BookHotel.objects.filter(username_id=user).filter(hotel_name=hotel).filter(date=date).filter(room=room)
    hotel.delete()
    return redirect('dashboard')

@login_required
def CancelPackage(request,flight=None,seat=None,hotel=None,date=None,room=None):
    flight = Flights.objects.filter(flight_num=flight)
    hotel = Hotels.objects.filter(hotel_name=hotel)
    for i in hotel:
        price = room*i.hotel_price
    for j in flight:
        price1 = seat*j.eprice
    f = {'Flight':flight}
    p = {'pricef':price1}
    s = {'seat':seat}
    h = {'Hotel':hotel}
    p1 = {'priceh':price}
    r = {'room':room}
    d = {'date':date}
    response = {**h,**p,**r,**d,**f,**p1,**s}
    return render(request,'cancelpackage.html',response)

@login_required
def ConfirmCancelPackage(request,flight=None,seat=None,hotel=None,date=None,room=None):
    user = request.user
    package = BookPackage.objects.filter(username_id=user).filter(hotel_name=hotel).filter(date=date).filter(room=room).filter(flight=flight).filter(seat=seat)
    package.delete()
    return redirect('dashboard')

def PlacesView(request):
    form = CityForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            city = form.cleaned_data['city']
            famplace = Famous.objects.filter(city__city__contains=city)
            f = {'form':form}
            p = {'Famplace':famplace}
            response = {**f,**p}
            return render(request,'places.html',response)
        else:
            return render(request,'places.html',{'form':form})
    else:
        return render(request,'places.html',{'form':form})
