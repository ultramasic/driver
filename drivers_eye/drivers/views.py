from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Driver
from .forms import DriverForm
from django.db import IntegrityError


@login_required
def driver_profile(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'drivers/driver_profile.html', {'driver': driver})

@login_required
def create_driver(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.save()
            if driver.truck:
                driver.assign_truck(driver.truck)
            if driver.asset:
                driver.assign_asset(driver.asset)
            return redirect('dashboard')
    else:
        form = DriverForm()
    return render(request, 'drivers/create_driver.html', {'form': form})

@login_required
def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            try:
                form.save()
                driver.assign_truck(driver.truck)
                return redirect('driver_profile', driver_id=driver.id)
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    form.add_error(None, 'This driver is already assigned to another truck.')
                else:
                    form.add_error(None, 'An error occurred while saving the driver.')
    else:
        form = DriverForm(instance=driver)
    
    return render(request, 'drivers/edit_driver.html', {'form': form, 'driver': driver})

@login_required
def delete_driver(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        driver.delete()
        return redirect('dashboard')
    return render(request, 'drivers/delete_driver.html', {'driver': driver})
