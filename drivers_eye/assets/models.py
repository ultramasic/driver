from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.apps import apps

class Asset(models.Model):
    license_plate = models.CharField(max_length=20, unique=True, default="UNKNOWN")
    vin = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    max_weight_capacity = models.IntegerField()
    gps_data = models.CharField(max_length=255, blank=True, null=True)
    length = models.IntegerField()
    truck = models.OneToOneField('trucks.Truck', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_asset')
    driver = models.OneToOneField('drivers.Driver', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_asset_truck')

    def __str__(self):
        return self.license_plate

    def assign_truck(self, truck):
        self.truck = truck
        if truck:
            truck.asset = self
            if truck.driver:
                self.driver = truck.driver
                truck.driver.asset = self
        self.save()
        if truck:
            truck.save()
            if truck.driver:
                truck.driver.save()

    def unassign_truck(self):
        if self.truck:
            self.truck.asset = None
            if self.driver:
                self.driver.asset = None
                self.driver.truck = None
                self.driver.save()
            self.truck.save()
        self.truck = None
        self.save()

    def assign_driver(self, driver):
        self.driver = driver
        if driver:
            driver.asset = self
            if driver.truck:
                self.truck = driver.truck
                driver.truck.asset = self
        self.save()
        if driver:
            driver.save()
            if driver.truck:
                driver.truck.save()

    def unassign_driver(self):
        if self.driver:
            self.driver.asset = None
            if self.truck:
                self.truck.driver = None
                self.truck.save()
            self.driver.truck = None
            self.driver.save()
        self.driver = None
        self.save()