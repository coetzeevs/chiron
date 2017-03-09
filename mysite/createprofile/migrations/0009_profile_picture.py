# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 16:20
from __future__ import unicode_literals

import createprofile.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('createprofile', '0008_auto_20170309_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.FileField(upload_to='documents/photos/', validators=[createprofile.validators.validate_photo_extension])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
