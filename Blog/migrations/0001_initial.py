# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=150)),
                ('post_text', models.CharField(max_length=15000)),
            ],
        ),
    ]
