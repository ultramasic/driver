# Generated by Django 5.0.7 on 2024-07-27 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
        ('drivers', '0001_initial'),
        ('trucks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='assign_driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver'),
        ),
        migrations.AddField(
            model_name='asset',
            name='assign_truck',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='trucks.truck'),
        ),
    ]
