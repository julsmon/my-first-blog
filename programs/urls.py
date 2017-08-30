from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'programs'


urlpatterns = [

    #frontend homepage
    url(r'^$', views.AllProgramsView.as_view(), name='index'),

    #register page
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    #login page
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='login'),

    #single program page
    url(r'^(?P<pk>[0-9]+)/$', views.ProgramDetailView.as_view(), name='program'),

    #bookmark a program as a favourite
    url(r'^(?P<program_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),

    #remove a program from favourite
    url(r'^(?P<program_id>[0-9]+)/unfavourite/$', views.unfavourite, name='unfavourite'),

    #program create page
    url(r'^program/create/$', views.ProgramCreate.as_view(template_name="programs/create.html"), name='program-create'),

    #program update page  url programs/program_id
    url(r'^program/(?P<pk>[0-9]+)/$', views.ProgramUpdate.as_view(template_name="programs/update.html"), name='program-update'),

    #program delete page  url programs/program_id/delete
    url(r'^program/(?P<pk>[0-9]+)/delete/$', views.ProgramDelete.as_view(), name='program-delete'),

    #cycle create page
    url(r'^cycle/create/$', views.CycleCreate.as_view(template_name="programs/cycle-create.html"), name='cycle-create'),

    #cycle update page
    url(r'^cycle/(?P<pk>[0-9]+)/$', views.CycleUpdate.as_view(template_name="programs/cycle-update.html"), name='cycle-update'),

    #cycle delete page
    url(r'^cycle/(?P<pk>[0-9]+)/delete/$', views.CycleDelete.as_view(), name='cycle-delete'),

    #step create page
    url(r'^step/create/$', views.StepCreate.as_view(template_name="programs/step-create.html"), name='step-create'),

    #step update page
    url(r'^step/(?P<pk>[0-9]+)/$', views.StepUpdate.as_view(template_name="programs/step-update.html"), name='step-update'),

    #step delete page
    url(r'^step/(?P<pk>[0-9]+)/delete/$', views.StepDelete.as_view(), name='step-delete'),

    #API (get) all programs related to a user
    url(r'^api/', views.AllProgramsApi.as_view()),

]




urlpatterns = format_suffix_patterns(urlpatterns)
