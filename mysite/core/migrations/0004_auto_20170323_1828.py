# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-23 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone_number',
            field=models.IntegerField(blank=True),
        ),
    ]
