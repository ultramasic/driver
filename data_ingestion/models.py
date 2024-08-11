from django.db import models

class RawData(models.Model):
    truck = models.ForeignKey('trucks.Truck', on_delete=models.CASCADE)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data for {self.truck} at {self.timestamp}"
