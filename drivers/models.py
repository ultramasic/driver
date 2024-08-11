from trucks.models import Truck
from assets.models import Asset
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.apps import apps

class Driver(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    drivers_license_number = models.CharField(max_length=100)
    drivers_license_issue_date = models.DateField()
    drivers_license_expiration_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    driver_score = models.FloatField(blank=True, null=True)
    fuel_usage = models.FloatField(blank=True, null=True)
    last_position = models.CharField(max_length=255, blank=True, null=True)
    latest_violation = models.CharField(max_length=255, blank=True, null=True)
    last_trip = models.CharField(max_length=255, blank=True, null=True)
    miles_driven = models.IntegerField(blank=True, null=True)
    truck = models.OneToOneField(Truck, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_driver')
    asset = models.OneToOneField(Asset, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_driver_asset')

    def __str__(self):
        return f"{self.name}"

    def assign_truck(self, truck):
        Truck.objects.filter(driver_id=self.id).update(driver=None)
        self.truck = truck
        if truck:
            truck.driver = self
            if truck.asset:
                self.asset = truck.asset
                truck.asset.driver = self
        self.save()
        if truck:
            truck.save()
            if truck.asset:
                truck.asset.save()

    def unassign_truck(self):
        if self.truck:
            self.truck.driver = None
            if self.truck.asset:
                self.asset = None
                self.truck.asset.driver = None
            self.truck.save()
            if self.truck.asset:
                self.truck.asset.save()
        self.truck = None
        self.save()

    def assign_asset(self, asset):
        self.asset = asset
        if asset:
            asset.driver = self
            if asset.truck:
                self.truck = asset.truck
                asset.truck.driver = self
        self.save()
        if asset:
            asset.save()
            if asset.truck:
                asset.truck.save()

    def unassign_asset(self):
        if self.asset:
            self.asset.driver = None
            if self.asset.truck:
                self.truck = None
                self.asset.truck.driver = None
            self.asset.save()
            if self.asset.truck:
                self.asset.truck.save()
        self.asset = None
        self.save()