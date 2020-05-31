# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openra', '0011_auto_20160511_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lints',
            name='lint_output',
            field=models.CharField(default='', max_length=10000000),
        ),
        migrations.AlterField(
            model_name='maps',
            name='base64_players',
            field=models.CharField(blank=True, default='', max_length=10000000, null=True),
        ),
        migrations.AlterField(
            model_name='maps',
            name='base64_rules',
            field=models.CharField(blank=True, default='', max_length=10000000, null=True),
        ),
    ]
