from django.contrib import admin
from .models import Profile, Location, Equipment, ManufacturerProfile

admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Equipment)
admin.site.register(ManufacturerProfile)
