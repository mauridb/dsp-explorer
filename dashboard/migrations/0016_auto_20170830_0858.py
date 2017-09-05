# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-30 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20170821_0945'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='organization',
            field=models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sector',
            field=models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='Sector'),
        ),
        migrations.AddField(
            model_name='profile',
            name='size',
            field=models.TextField(blank=True, default='', max_length=200, null=True, verbose_name='Size'),
        ),
        migrations.AddField(
            model_name='profile',
            name='social_links',
            field=models.TextField(blank=True, default='[{"name":"twitter","link":""},{"name":"google-plus","link":""},{"name":"facebook","link":""}]', max_length=200, null=True, verbose_name='Size'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tags',
            field=models.ManyToManyField(related_name='profile_tags', to='dashboard.Tag'),
        ),
    ]