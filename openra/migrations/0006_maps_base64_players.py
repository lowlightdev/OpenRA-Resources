# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openra', '0005_maps_base64_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='maps',
            name='base64_players',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
    ]
