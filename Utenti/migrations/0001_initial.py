# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 09:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('washing_machine_brand', models.CharField(max_length=50)),
                ('washing_machine_model', models.CharField(max_length=50)),
                ('washing_machine_serial_number', models.CharField(max_length=100)),
                ('washing_machine_capacity', models.CharField(max_length=50)),
                ('cpu_model_on_washing_machine', models.CharField(max_length=50)),
                ('cpu_serial_number_on_washing_machine', models.CharField(max_length=50)),
                ('power_board_model_on_washing_machine', models.CharField(max_length=50)),
                ('power_board_serial_number_on_washing_machine', models.CharField(max_length=50)),
                ('dryer_machine_brand', models.CharField(max_length=50)),
                ('dryer_machine_model', models.CharField(max_length=50)),
                ('dryer_machine_serial_number', models.CharField(max_length=50)),
                ('dryer_machine_capacity', models.CharField(max_length=50)),
                ('cpu_model_on_dryer', models.CharField(max_length=50)),
                ('cpu_serial_number_on_dryer', models.CharField(max_length=50)),
                ('power_board_model_on_dryer', models.CharField(max_length=50)),
                ('power_board_serial_number_on_dryer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100)),
                ('location_address', models.CharField(max_length=100)),
                ('location_city', models.CharField(max_length=100)),
                ('location_zip_code', models.CharField(max_length=50)),
                ('location_state', models.CharField(max_length=50)),
                ('location_country', models.CharField(max_length=50)),
                ('location_IP', models.GenericIPAddressField()),
                ('location_gateway', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ManufacturerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
                ('bio', models.TextField(max_length=500)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=500)),
                ('company_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Utenti.Location'),
        ),
    ]
