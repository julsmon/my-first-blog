from django.shortcuts import render
from .models import Profile, Location, Equipment, ManufacturerProfile
from .forms import ProfileFormClass, ProfileForm, LocationFormClass, LocationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from . import urls

#Welcome view for users, displaying ProfileForm
class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileFormClass

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(ProfileCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('utenti:location', args=())


#Location view for users, displaying LocationForm
class LocationCreate(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationFormClass

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(LocationCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('utenti:home', args=())
