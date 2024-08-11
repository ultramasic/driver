from django import forms
from .models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['license_plate', 'vin', 'year', 'make', 'model', 'max_weight_capacity', 'truck', 'driver', 'length']

    def clean(self):
        cleaned_data = super().clean()
        truck = cleaned_data.get('truck')
        driver = cleaned_data.get('driver')

        if truck and not driver:
            if truck.driver:
                cleaned_data['driver'] = truck.driver

        if driver and not truck:
            if driver.truck:
                cleaned_data['truck'] = driver.truck

        return cleaned_data