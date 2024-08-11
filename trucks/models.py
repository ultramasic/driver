from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.apps import apps


class Truck(models.Model):
    license_plate = models.CharField(max_length=20, unique=True, default="UNKNOWN")
    vin = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    mileage = models.IntegerField()
    fuel_tank_capacity = models.IntegerField()
    last_trip = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    obdii_fault_codes = models.CharField(max_length=255, blank=True, null=True)
    fuel_level = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    rpm = models.IntegerField(blank=True, null=True)
    engine_temperature = models.IntegerField(blank= True, null=True)
    engine_load = models.IntegerField(blank=True, null=True)
    live_fuel_usage = models.FloatField(blank=True, null=True)
    gps_data = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    driver = models.OneToOneField('drivers.Driver', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_truck')
    asset = models.OneToOneField('assets.Asset', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_truck_asset')

    def __str__(self):
        return self.license_plate

    def assign_driver(self, driver):
        self.driver = driver
        if driver:
            driver.truck = self
            if self.asset:
                driver.asset = self.asset
                self.asset.driver = driver
        self.save()
        if driver:
            driver.save()
            if self.asset:
                self.asset.save()

    def unassign_driver(self):
        if self.driver:
            self.driver.truck = None
            if self.asset:
                self.driver.asset = None
                self.asset.driver = None
            self.driver.save()
            if self.asset:
                self.asset.save()
        self.driver = None
        self.save()

    def assign_asset(self, asset):
        self.asset = asset
        if asset:
            asset.truck = self
            if self.driver:
                asset.driver = self.driver
                self.driver.asset = asset
        self.save()
        if asset:
            asset.save()
            if self.driver:
                self.driver.save()

    def unassign_asset(self):
        if self.asset:
            self.asset.truck = None
            if self.driver:
                self.asset.driver = None
                self.driver.asset = None
            self.asset.save()
            if self.driver:
                self.driver.save()
        self.asset = None
        self.save()