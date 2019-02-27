# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-02-12 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20190205_1055'),
        ('courses', '0007_video_video_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='\u8bfe\u7a0b\u8bb2\u5e08'),
        ),
    ]