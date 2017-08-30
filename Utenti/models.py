from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    company_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

#    """This handles the redirect of the ModelForm related to this model"""
#    def get_absolute_url(self):
#        return reverse('Utenti:connection')

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=100)
    location_address = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_zip_code = models.CharField(max_length=50)
    location_state = models.CharField(max_length=50)
    location_country = models.CharField(max_length=50)
    location_IP = models.GenericIPAddressField()
    location_gateway = models.CharField(max_length=25)

#@receiver(post_save, sender=User)
#def create_user_location(sender, instance, created, **kwargs):
#    if created:
#        Location.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_location(sender, instance, **kwargs):
#    instance.location.save()

class Equipment(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    washing_machine_brand = models.CharField(max_length=50)
    washing_machine_model = models.CharField(max_length=50)
    washing_machine_serial_number = models.CharField(max_length=100)
    washing_machine_capacity = models.CharField(max_length=50)
    cpu_model_on_washing_machine = models.CharField(max_length=50)
    cpu_serial_number_on_washing_machine = models.CharField(max_length=50)
    power_board_model_on_washing_machine = models.CharField(max_length=50)
    power_board_serial_number_on_washing_machine = models.CharField(max_length=50)
    dryer_machine_brand = models.CharField(max_length=50)
    dryer_machine_model = models.CharField(max_length=50)
    dryer_machine_serial_number = models.CharField(max_length=50)
    dryer_machine_capacity = models.CharField(max_length=50)
    cpu_model_on_dryer = models.CharField(max_length=50)
    cpu_serial_number_on_dryer = models.CharField(max_length=50)
    power_board_model_on_dryer = models.CharField(max_length=50)
    power_board_serial_number_on_dryer = models.CharField(max_length=50)


class ManufacturerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
