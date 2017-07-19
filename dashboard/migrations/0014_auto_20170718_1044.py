# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-18 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_profile_twitter_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='Picture'),
        ),
    ]
