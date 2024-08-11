from django import forms
from .models import Truck

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['license_plate', 'vin', 'year', 'make', 'model', 'fuel_type', 'mileage', 'fuel_tank_capacity', 'asset', 'driver']

    def clean(self):
        cleaned_data = super().clean()
        driver = cleaned_data.get('driver')
        asset = cleaned_data.get('asset')

        if driver and not asset:
            if driver.asset:
                cleaned_data['asset'] = driver.asset

        if asset and not driver:
            if asset.driver:
                cleaned_data['driver'] = asset.driver

        return cleaned_data