# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-07 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openra', '0009_auto_20160404_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='base64_players',
            field=models.CharField(blank=True, default='', max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='maps',
            name='base64_rules',
            field=models.CharField(blank=True, default='', max_length=1000000, null=True),
        ),
    ]
