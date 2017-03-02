from django.conf.urls import url

from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^home/', views.home, name='home'),
]