from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .validators import validate_cv_extension, validate_photo_extension


class Employee_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_company = models.TextField(max_length=100, blank=True)
    previous_company = models.TextField(max_length=100, blank=True)
    highest_qualification =  models.TextField(max_length=100, blank=True)
    institute_hq =  models.TextField(max_length=100, blank=True)
    highschool = models.TextField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    sql = models.BooleanField(default = False)
    python = models.BooleanField(default = False)
    r = models.BooleanField(default = False)
    scala = models.BooleanField(default = False)
    julia  = models.BooleanField(default = False)
    tableau = models.BooleanField(default = False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Employee_Profile._meta.fields]
    
class Employer_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.TextField(max_length=30, blank=True)
    industry = models.TextField(max_length=30, blank=True)
    bio =  models.TextField(max_length=500, blank=True)
    url =  models.TextField(max_length=50, blank=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Employer_Profile._meta.fields]

class Document(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to="documents/", validators=[validate_cv_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    

class Profile_Picture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="documents/photos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Logo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="documents/photos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to="documents/jobs/", validators=[validate_cv_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    