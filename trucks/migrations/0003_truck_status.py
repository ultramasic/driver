# Generated by Django 5.0.7 on 2024-07-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0002_remove_truck_assign_asset_remove_truck_assign_driver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
