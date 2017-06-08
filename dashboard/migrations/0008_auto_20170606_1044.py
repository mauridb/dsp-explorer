# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20170606_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='profile',
        ),
        migrations.AddField(
            model_name='invitation',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Profile'),
        ),
    ]