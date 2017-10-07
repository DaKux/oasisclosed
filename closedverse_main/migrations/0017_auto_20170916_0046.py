# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-16 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closedverse_main', '0016_profile_no_let_yeahnotifs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='no_let_yeahnotifs',
        ),
        migrations.AddField(
            model_name='profile',
            name='let_yeahnotifs',
            field=models.BooleanField(default=True),
        ),
    ]
