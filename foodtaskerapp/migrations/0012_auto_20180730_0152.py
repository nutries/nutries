# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-30 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0011_auto_20180730_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
