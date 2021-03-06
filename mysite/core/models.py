from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    employer = models.BooleanField(default = False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Profile._meta.fields]

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class ContactUs(models.Model):
    surname = models.TextField(max_length=30, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    subject = models.TextField(max_length=1000, blank=False)
    email_body = models.TextField(max_length=2000, blank=False)
    phone_number = models.IntegerField(blank=True)
    current_occupation = models.TextField(max_length=500, blank=True)
    location = models.TextField(max_length=500, blank=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ContactUs._meta.fields]
