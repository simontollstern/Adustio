# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 12:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20170619_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 20, 12, 45, 30, 53977, tzinfo=utc)),
        ),
    ]