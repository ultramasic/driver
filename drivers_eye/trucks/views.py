from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Truck
from .forms import TruckForm
from django.http import JsonResponse


@login_required
def truck_profile(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    return render(request, 'trucks/truck_profile.html', {'truck': truck})


def serialize_truck(truck):
    return {
        'lat': float(truck.latitude),
        'lng': float(truck.longitude),
        'name': truck.license_plate,
        'driver': truck.driver.name if truck.driver else None,
        'fuel_level': truck.fuel_level,
        'speed': truck.speed
    }

@login_required
def create_truck(request):
    if request.method == "POST":
        form = TruckForm(request.POST)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.save()
            if truck.driver:
                truck.assign_driver(truck.driver)
            if truck.asset:
                truck.assign_asset(truck.asset)
            return redirect('dashboard')
    else:
        form = TruckForm()
    return render(request, 'trucks/create_truck.html', {'form': form})

@login_required
def edit_truck(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    if request.method == "POST":
        form = TruckForm(request.POST, instance=truck)
        if form.is_valid():
            truck = form.save(commit=False)
            truck.save()
            if truck.driver:
                truck.assign_driver(truck.driver)
            if truck.asset:
                truck.assign_asset(truck.asset)
            return redirect('dashboard')
    else:
        form = TruckForm(instance=truck)
    return render(request, 'trucks/edit_truck.html', {'form': form})

@login_required
def delete_truck(request, pk):
    truck = get_object_or_404(Truck, pk=pk)
    if request.method == "POST":
        truck.delete()
        return redirect('dashboard')
    return render(request, 'trucks/delete_truck.html', {'truck': truck})

@login_required
def truck_data(request):
    trucks = Truck.objects.all()
    trucks_data = [serialize_truck(truck) for truck in trucks if truck.latitude is not None and truck.longitude is not None]
    return JsonResponse(trucks_data, safe=False)


