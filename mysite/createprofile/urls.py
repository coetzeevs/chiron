from django.conf.urls import url

from . import views

app_name = 'createprofile'
urlpatterns = [
    url(r'^employee/$', views.index, name='index'),
    url(r'^employer/$', views.emplyer_create_profile, name='emplyer_create_profile'),
    url(r'^employer/edit/$', views.emplyer_edit_profile, name='emplyer_edit_profile'),
]
