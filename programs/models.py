from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class MotorSetting(models.Model):
    """Definzione dati motore"""
    """scelta del motore, da 1 a 6"""
    motor_number = models.CharField(max_length=50, unique=True, choices=[('Motor 1','Motor 1'), ('Motor 2','Motor 2'), ('Motor 3','Motor 3'), ('Motor 4', 'Motor 4'), ('Motor 5','Motor 5'), ('Motor 6','Motor 6'), ('Motor 7','Motor 7'), ('Motor 8','Motor 8'), ('Motor 9','Motor 9'), ('Motor 10','Motor 10'), ('Motor 11','Motor 11'), ('Motor 12','Motor 12'), ('Motor 13','Motor 13'), ('Motor 14','Motor 14'), ('Motor 15','Motor 15')])
    """tempo di rotazione in avanti, espresso in secondi"""
    forward_motion_time = models.IntegerField(

    )
    """tempo di pausa del motore, espresso in secondo"""
    pause_motion_time = models.IntegerField(

    )
    """tempo di rotazione inversa, espresso in secondi"""
    backward_motion_time = models.IntegerField(

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.motor_number

class Output24(models.Model):
    output_position = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.output_position


class CustomRelay(models.Model):
    crelay_name = models.CharField("Custom Relay, Name", max_length=50)
    crelay_description = models.CharField("Custom Relay, Description", max_length=150)
    output = models.OneToOneField(Output24)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.crelay_name

class WaterInlet(models.Model):
    water_inlet_name = models.CharField("Water Type", max_length=50)
    water_inlet_description = models.CharField("Description of the inlet valve", max_length=150)
    output = models.OneToOneField(Output24)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.water_inlet_name


class Chemical(models.Model):
    chemical_name = models.CharField("Chemical Name", max_length=50)
    chemical_description = models.CharField("Chemical Description", max_length=150)
    output = models.OneToOneField(Output24)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.chemical_name

class Step(models.Model):
    """definizione del database che contiene gli step programmabili dall'utente"""
    step_name = models.CharField(max_length=50)
    step_description = models.TextField(max_length=250)
    water_inlet = models.ForeignKey(WaterInlet, blank=True, null=True)
    drain = models.CharField(max_length=30, choices=[('False', 'No'),('True', 'Yes')], blank=True, null=True)
    chemicals = models.ManyToManyField(Chemical)
    custom_relays = models.ManyToManyField(CustomRelay)
    """scelta del tipo di motore, da 1 a 15"""
    motor = models.ForeignKey(MotorSetting, on_delete=models.CASCADE)
    """assegnazione velocità motore espressa in giri al minuto"""
    motor_speed = models.IntegerField(
        validators=[MaxValueValidator(999), MinValueValidator(0)],
        blank=True,
        null=True
    )
    """settaggio fine step"""
    """livello"""
    stop_level = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        blank=True,
        null=True
    )
    """temperatura"""
    stop_temperature = models.IntegerField(
        validators=[MaxValueValidator(93), MinValueValidator(2)],
        blank=True,
        null=True
    )
    """tempo"""
    stop_time = models.IntegerField(
        blank=True,
        null=True
    )
    """watchdog"""
    wdt = models.IntegerField(
        blank=True,
        null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.step_name + "  --  " + self.step_description

class Cycle(models.Model):
    """Definizione dei cicli liberamente configurabili. Ogni ciclo è composto da uno o più step"""
    cycle_type = models.CharField(max_length=150, choices=[('Pre-wash', 'Pre-wash'), ('Wash', 'Wash'), ('Rinse', 'Rinse'), ('Spin', 'Spin'), ('Unroll', 'Unroll')])
    cycle_name = models.CharField(max_length=250)
    cycle_description = models.CharField(max_length=250)
    steps = models.ManyToManyField(Step)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.cycle_name + "  --  " + self.cycle_description

class Program(models.Model):
    """Definizione dei programmi liberamente configurabili. Ogni programma si compone di uno o più cicli predefiniti dal Cliente"""
    program_name = models.CharField(max_length=50)
    program_description = models.CharField(max_length=250)
    cycles = models.ManyToManyField(Cycle)
    is_favourite = models.BooleanField(default="False")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('programs:program', kwargs={'pk': self.pk})

    def __str__(self):
        return self.program_name


class GeneralSetting(models.Model):
    """Definizione dei parametri generali"""
    language = models.CharField(max_length=100, choices=[('English', 'English'),('Italiano', 'Italiano'),('Español', 'Español'), ('Français', 'Français'), ('Deutsch', 'Deutsch')])
    degrees = models.CharField(max_length=100, choices=[('Celsius (C°)', 'Celsius (C°)'), ('Farenheit (F°)', 'Farenheit (F°)')])
    """Definizione dei settaggi base della macchina"""
    """Livello massimo di riscaldamento"""
    heat_max = models.IntegerField(

    )
    """Livello massimo di raffreddamento"""
    cool_max = models.IntegerField(

    )
    """Livello massimo di velocità del motore"""
    speed_max = models.IntegerField(

    )
    """Tempo di rallentamento centrifuga"""
    spin_braking = models.IntegerField(

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class LogsParameter(models.Model):
    """Definizione dei parametri per log e analytics"""
    """Tempo di funzionamento espresso in ore"""
    uptime_hours = models.IntegerField
    """Tempo di inattività espresso in ore"""
    downtime_hours = models.IntegerField
    """Numero di lavaggi eseguiti al momento della richiesta"""
    num_washes_performed = models.IntegerField
    """Numero di errori visualizzati"""
    num_errors_displayed = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE)
