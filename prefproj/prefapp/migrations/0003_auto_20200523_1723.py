# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-23 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prefapp', '0002_auto_20200523_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mnumber',
            field=models.CharField(max_length=12),
        ),
    ]
