from django.contrib.auth.models import User
from django import forms
from .models import Profile, Location, Equipment, ManufacturerProfile


#creating a class to bootstrap profile form on frontend
class ProfileFormClass(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileFormClass, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg'
        })

    class Meta:
        model = Profile
        fields = ('bio', 'company_name', 'address', 'city', 'zip_code', 'state', 'country')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'company_name', 'address', 'city', 'zip_code', 'state', 'country')



#creating a class to bootstrap location form on frontend
class LocationFormClass(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LocationFormClass, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg'
        })

    class Meta:
        model = Location
        fields = ('location_name', 'location_address', 'location_city', 'location_zip_code', 'location_state', 'location_country', 'location_IP', 'location_gateway')

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ('location_name', 'location_address', 'location_city', 'location_zip_code', 'location_state', 'location_country', 'location_IP', 'location_gateway')
