# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openra', '0008_auto_20160329_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maps',
            name='base64_players',
            field=models.CharField(blank=True, default='', max_length=100000, null=True),
        ),
    ]
