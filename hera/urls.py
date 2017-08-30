from django.conf.urls import include, url
from django.contrib import admin
from programs import urls
from programs import views
from django.contrib.auth import views as auth_views
from base import urls


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    #login page
    url(r'^$', auth_views.LoginView.as_view(), name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^programs/', include('programs.urls', namespace="programs")),
    url(r'^signup/', views.UserFormView.as_view(), name='register'),
    url(r'', include('Utenti.urls', namespace='utenti')),
    url(r'', include('base.urls', namespace='base'))
]
