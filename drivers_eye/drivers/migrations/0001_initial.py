# Generated by Django 5.0.7 on 2024-07-27 12:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('drivers_license_number', models.CharField(max_length=20, unique=True)),
                ('drivers_license_expiration_date', models.DateField()),
                ('drivers_license_issue_date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('driver_score', models.FloatField(blank=True, null=True)),
                ('fuel_usage', models.FloatField(blank=True, null=True)),
                ('last_position', models.CharField(blank=True, max_length=255)),
                ('latest_violation', models.CharField(blank=True, max_length=255)),
                ('last_trip', models.CharField(blank=True, max_length=255)),
                ('miles_driven', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
