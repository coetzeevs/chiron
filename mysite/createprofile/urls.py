from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'createprofile'
urlpatterns = [
    url(r'^employee/$', views.index, name='index'),
    url(r'^employer/$', views.emplyer_create_profile, name='emplyer_create_profile'),
    url(r'^employer/edit/$', views.emplyer_edit_profile, name='emplyer_edit_profile'),
    url(r'^employee/edit/$', views.emplyee_edit_profile, name='emplyee_edit_profile'),
    url(r'^employee/home/$', views.employee_home, name='employee_home'),
    url(r'^employee/view_profile/$', views.employee_view_profile, name='employee_view_profile'),
    url(r'^employee/uploadcv/$', views.model_form_upload, name='model_form_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
