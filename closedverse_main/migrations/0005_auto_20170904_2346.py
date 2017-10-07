# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-04 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0004_auto_20170902_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='is_rm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='addr',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
