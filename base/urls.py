from django.conf.urls import url
from . import views

app_name = 'base'


urlpatterns = [

    #home page
    url(r'^home/$', views.home, name='home'),


]
