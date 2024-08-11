from django import forms
from .models import Driver

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'date_of_birth', 'truck', 'drivers_license_number', 'drivers_license_expiration_date', 'drivers_license_issue_date', 'phone_number']
    

    def clean(self):
        cleaned_data = super().clean()
        truck = cleaned_data.get('truck')
        asset = cleaned_data.get('asset')

        if truck and not asset:
            if truck.asset:
                cleaned_data['asset'] = truck.asset

        if asset and not truck:
            if asset.truck:
                cleaned_data['truck'] = asset.truck

        return cleaned_data