from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegistrationForm, CompanyRegistrationForm
from .models import CustomUser, Company
import json
from django.urls import reverse, NoReverseMatch
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from trucks.models import Truck
from drivers.models import Driver
from assets.models import Asset


def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            email = request.POST.get('username')
            password = request.POST.get('password')
        
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Email or password is wrong'})
    
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register_company')
        else:
            messages.error(request, "Invalid registration details.")
    form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def register_company(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, "Invalid company details.")
    form = CompanyRegistrationForm()
    companies = Company.objects.all()
    return render(request, 'accounts/register_company.html', {'form': form, 'companies': companies})

def logout_view(request):
    logout(request)
    return redirect('login')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if CustomUser.objects.filter(email=email).exists():
            messages.success(request, "A link to reset your password has been sent to your email.")
        else:
            messages.error(request, "Email not registered.")
        return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html')

@login_required
def dashboard(request):
    trucks = Truck.objects.all()
    drivers = Driver.objects.all()
    assets = Asset.objects.all()
    return render(request, 'accounts/dashboard.html', {'trucks': trucks, 'drivers': drivers, 'assets': assets})


def serialize_driver(driver):
    return {
        'name': driver.name
    }

@login_required
def fleet_view(request):
    trucks = Truck.objects.all()
    drivers = Driver.objects.all()
    assets = Asset.objects.all()
    
    google_maps_api_key = 'AIzaSyCoL-BK7NQxqOsgPfOlakj_hmLqhlMZr4I'
    
    trucks_js = [
        {
            'lat': float(truck.latitude),
            'lng': float(truck.longitude),
            'name': truck.license_plate,
            'driver': truck.driver if truck.driver else None,
            'fuel_level': truck.fuel_level,
            'speed': truck.speed
        }
        for truck in trucks if truck.latitude is not None and truck.longitude is not None
    ]

    try:
        truck_data_url = request.build_absolute_uri(reverse('truck_data'))
    except NoReverseMatch:
        truck_data_url = None

    context = {
        'trucks': trucks,
        'drivers': drivers,
        'assets': assets,
        'google_maps_api_key': google_maps_api_key,
        'trucks_js': trucks_js,
        'truck_data_url': truck_data_url
    }
    
    return render(request, 'accounts/fleet_view.html', context)