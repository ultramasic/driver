from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Asset
from .forms import AssetForm


@login_required
def asset_profile(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    return render(request, 'assets/asset_profile.html', {'asset': asset})

@login_required
def create_asset(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            if asset.truck:
                asset.assign_truck(asset.truck)
            if asset.driver:
                asset.assign_driver(asset.driver)
            return redirect('dashboard')
    else:
        form = AssetForm()
    return render(request, 'assets/create_asset.html', {'form': form})

@login_required
def edit_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == "POST":
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.save()
            if asset.truck:
                asset.assign_truck(asset.truck)
            if asset.driver:
                asset.assign_driver(asset.driver)
            return redirect('dashboard')
    else:
        form = AssetForm(instance=asset)
    return render(request, 'assets/edit_asset.html', {'form': form})

@login_required
def delete_asset(request, pk):
    asset = get_object_or_404(Asset, pk=pk)
    if request.method == 'POST':
        asset.delete()
        return redirect('dashboard')
    return render(request, 'assets/delete_asset.html', {'asset': asset})
