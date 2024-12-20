# Generated by Django 5.0.7 on 2024-07-27 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_remove_asset_assign_driver_remove_asset_assign_truck_and_more'),
        ('drivers', '0002_initial'),
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='assign_vehicle',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='created_at',
        ),
        migrations.AddField(
            model_name='driver',
            name='asset',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_driver_asset', to='assets.asset'),
        ),
        migrations.AddField(
            model_name='driver',
            name='truck',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_driver', to='trucks.truck'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='drivers_license_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_trip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='latest_violation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='miles_driven',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
