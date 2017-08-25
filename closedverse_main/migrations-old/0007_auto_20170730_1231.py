# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-30 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0006_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='origin_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='origin_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]