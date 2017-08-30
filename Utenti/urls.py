from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'Utenti'


urlpatterns = [

    #welcome page, displaying profile creation form
    url(r'^welcome/$', views.ProfileCreate.as_view(template_name="utenti/profile-form.html"), name='welcome'),
    #location page, displaying location creation form
    url(r'^location/$', views.LocationCreate.as_view(template_name="utenti/location-form.html"), name='location'),




]




urlpatterns = format_suffix_patterns(urlpatterns)
