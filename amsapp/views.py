from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Slot, Booking, reg_tbl
from django.shortcuts import render
from .models import Booking


# ----- Login -----
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == "admin123@gmail.com" and password == "admin123":
            request.session['is_admin'] = True
            return redirect('admin_dashboard')
           
        try:
            user = reg_tbl.objects.get(email=email, password=password)
            request.session['reg_id'] = user.id
            return redirect('user_dashboard')
        except reg_tbl.DoesNotExist:
            messages.error(request, "Invalid Email or Password !!!")
            return redirect('login')
    return render(request, 'login.html')

# ----- Registration -----
def reg(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password != cpassword:
            messages.error(request, "Passwords do not match!")
            return render(request, 'reg.html')

        user = reg_tbl.objects.create(fname=name, email=email, phone=phone, password=password, cpassword=cpassword)
        messages.success(request, "Registration successful! Please login.")
        return redirect('login')
    return render(request, 'reg.html')

# ----- User Dashboard -----
def user_dashboard(request):
    reg_id = request.session.get('reg_id')
    if not reg_id:
        return redirect('login')
    return render(request, 'user_dashboard.html')

# ----- Available Slots -----
def available_slots(request):
    reg_id = request.session.get('reg_id')
    if not reg_id:
        return redirect('login')

    slots = Slot.objects.all().order_by('date', 'time')
    return render(request, 'available_slots.html', {'slots': slots})

# ----- Book Slot via AJAX -----
def book_slot(request, slot_id):
    if request.method != 'POST':
        return JsonResponse({'status':'error', 'message':'Invalid request method.'})

    reg_id = request.session.get('reg_id')
    if not reg_id:
        return JsonResponse({'status':'error', 'message':'User not logged in.'})

    current_user = get_object_or_404(reg_tbl, id=reg_id)
    slot = get_object_or_404(Slot, id=slot_id)

    if slot.is_booked:
        return JsonResponse({'status':'error','message':'Slot already booked.'})

    
    Booking.objects.create(user=current_user, slot=slot, status='booked')
    slot.is_booked = True
    slot.save()

    return JsonResponse({'status':'success','message':'Slot booked successfully!'})

# ----- My Bookings -----
def my_bookings(request):
    reg_id = request.session.get('reg_id')
    if not reg_id:
        return redirect('login')

    current_user = get_object_or_404(reg_tbl, id=reg_id)
    bookings = Booking.objects.filter(user=current_user).select_related('slot').order_by('-slot__date', '-slot__time')

    return render(request, 'my_bookings.html', {'bookings': bookings})

def base(request):
    return render(request,'base.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def manage_slots(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        description = request.POST['description']
        Slot.objects.create(date=date, time=time, description=description)
        return redirect('manage_slots')

    slots = Slot.objects.all()
    return render(request, 'manage_slots.html', {'slots': slots})
    
def manage_bookings(request):
    # Fetch all bookings along with related slots and users
    bookings = Booking.objects.select_related('user', 'slot').order_by('-slot__date', '-slot__time')
    
    return render(request, 'manage_bookings.html', {'bookings': bookings})


def base_user(request):
    return render(request,'base_user.html')

def cancel_booking(request, booking_id):
    if request.method != 'POST':
        return JsonResponse({'status':'error','message':'Invalid request method'})

    reg_id = request.session.get('reg_id')
    if not reg_id:
        return JsonResponse({'status':'error','message':'User not logged in'})

    booking = get_object_or_404(Booking, id=booking_id, user_id=reg_id)
    booking.status = 'canceled'
    booking.save()

    # Free the slot
    booking.slot.is_booked = False
    booking.slot.save()

    return JsonResponse({'status':'success','message':'Booking canceled successfully'})


def admin_cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = 'canceled'
    booking.save()
    booking.slot.is_booked = False
    booking.slot.save()
    return redirect('manage_bookings')


def logout_view(request):
    
    request.session.flush()

    return redirect('login')


