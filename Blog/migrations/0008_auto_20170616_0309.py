# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 01:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20170616_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 6, 16, 3, 9, 18, 236000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='dateAndTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 16, 3, 9, 18, 236000)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.TimeField(default=datetime.datetime(2017, 6, 16, 3, 9, 18, 236000)),
        ),
    ]
