# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 08:31
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemical_name', models.CharField(max_length=50, verbose_name='Chemical Name')),
                ('chemical_description', models.CharField(max_length=150, verbose_name='Chemical Description')),
            ],
        ),
        migrations.CreateModel(
            name='CustomRelay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crelay_name', models.CharField(max_length=50, verbose_name='Custom Relay, Name')),
                ('crelay_description', models.CharField(max_length=150, verbose_name='Custom Relay, Description')),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_type', models.CharField(choices=[('Pre-wash', 'Pre-wash'), ('Wash', 'Wash'), ('Rinse', 'Rinse'), ('Spin', 'Spin'), ('Unroll', 'Unroll')], max_length=150)),
                ('cycle_name', models.CharField(max_length=250)),
                ('cycle_description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('English', 'English'), ('Italiano', 'Italiano'), ('Español', 'Español'), ('Français', 'Français'), ('Deutsch', 'Deutsch')], max_length=100)),
                ('degrees', models.CharField(choices=[('Celsius (C°)', 'Celsius (C°)'), ('Farenheit (F°)', 'Farenheit (F°)')], max_length=100)),
                ('heat_max', models.IntegerField()),
                ('cool_max', models.IntegerField()),
                ('speed_max', models.IntegerField()),
                ('spin_braking', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LogsParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MotorSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motor_number', models.CharField(choices=[('Motor 1', 'Motor 1'), ('Motor 2', 'Motor 2'), ('Motor 3', 'Motor 3'), ('Motor 4', 'Motor 4'), ('Motor 5', 'Motor 5'), ('Motor 6', 'Motor 6'), ('Motor 7', 'Motor 7'), ('Motor 8', 'Motor 8'), ('Motor 9', 'Motor 9'), ('Motor 10', 'Motor 10'), ('Motor 11', 'Motor 11'), ('Motor 12', 'Motor 12'), ('Motor 13', 'Motor 13'), ('Motor 14', 'Motor 14'), ('Motor 15', 'Motor 15')], max_length=50, unique=True)),
                ('forward_motion_time', models.IntegerField()),
                ('pause_motion_time', models.IntegerField()),
                ('backward_motion_time', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Output24',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_position', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=50)),
                ('program_description', models.CharField(max_length=250)),
                ('is_favourite', models.BooleanField(default='False')),
                ('cycles', models.ManyToManyField(to='programs.Cycle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_name', models.CharField(max_length=50)),
                ('step_description', models.TextField(max_length=250)),
                ('drain', models.CharField(blank=True, choices=[('False', 'No'), ('True', 'Yes')], max_length=30, null=True)),
                ('motor_speed', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)])),
                ('stop_level', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('stop_temperature', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(93), django.core.validators.MinValueValidator(2)])),
                ('stop_time', models.IntegerField(blank=True, null=True)),
                ('wdt', models.IntegerField(blank=True, null=True)),
                ('chemicals', models.ManyToManyField(blank=True, null=True, to='programs.Chemical')),
                ('custom_relays', models.ManyToManyField(blank=True, null=True, to='programs.CustomRelay')),
                ('motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.MotorSetting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WaterInlet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_inlet_name', models.CharField(max_length=50, verbose_name='Water Type')),
                ('water_inlet_description', models.CharField(max_length=150, verbose_name='Description of the inlet valve')),
                ('output', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='programs.Output24')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='water_inlet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='programs.WaterInlet'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='steps',
            field=models.ManyToManyField(to='programs.Step'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customrelay',
            name='output',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='programs.Output24'),
        ),
        migrations.AddField(
            model_name='customrelay',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chemical',
            name='output',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='programs.Output24'),
        ),
        migrations.AddField(
            model_name='chemical',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
