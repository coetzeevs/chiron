# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 09:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('createprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(blank=True, max_length=30)),
                ('industry', models.TextField(blank=True, max_length=30)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('url', models.TextField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]