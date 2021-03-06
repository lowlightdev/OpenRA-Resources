# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 07:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000)),
                ('item_type', models.CharField(default='maps', max_length=16)),
                ('item_id', models.IntegerField(default=0)),
                ('posted', models.DateTimeField(verbose_name='date of comment')),
                ('is_removed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='CrashReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gameID', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=400)),
                ('isdesync', models.BooleanField(default=False)),
                ('gistID', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'CrashReport',
            },
        ),
        migrations.CreateModel(
            name='Lints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(default='maps', max_length=16)),
                ('map_id', models.IntegerField(default=0)),
                ('version_tag', models.CharField(default='release-20141029', max_length=100)),
                ('pass_status', models.BooleanField(default=False)),
                ('lint_output', models.CharField(default='', max_length=1000000)),
                ('posted', models.DateTimeField(verbose_name='date of check')),
            ],
            options={
                'verbose_name': 'Lint',
            },
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=4000)),
                ('info', models.CharField(max_length=4000)),
                ('author', models.CharField(max_length=200)),
                ('map_type', models.CharField(max_length=100)),
                ('players', models.IntegerField(default=0)),
                ('game_mod', models.CharField(max_length=100)),
                ('map_hash', models.CharField(max_length=200)),
                ('width', models.CharField(max_length=16)),
                ('height', models.CharField(max_length=16)),
                ('bounds', models.CharField(default='', max_length=50)),
                ('tileset', models.CharField(max_length=50)),
                ('spawnpoints', models.CharField(default='', max_length=1000)),
                ('mapformat', models.IntegerField(default=6)),
                ('parser', models.CharField(default='release-20141029', max_length=100)),
                ('shellmap', models.BooleanField(default=False)),
                ('legacy_map', models.BooleanField(default=False)),
                ('revision', models.IntegerField(default=1)),
                ('pre_rev', models.IntegerField(default=0)),
                ('next_rev', models.IntegerField(default=0)),
                ('downloading', models.BooleanField(default=True)),
                ('requires_upgrade', models.BooleanField(default=False)),
                ('advanced_map', models.BooleanField(default=False)),
                ('lua', models.BooleanField(default=False)),
                ('posted', models.DateTimeField(verbose_name='date published')),
                ('viewed', models.IntegerField(default=0)),
                ('downloaded', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('rsync_allow', models.BooleanField(default=True)),
                ('amount_reports', models.IntegerField(default=0)),
                ('policy_cc', models.BooleanField(default=False)),
                ('policy_adaptations', models.CharField(max_length=30)),
                ('policy_commercial', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Map',
            },
        ),
        migrations.CreateModel(
            name='Mods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=2000)),
                ('revision', models.IntegerField(default=1)),
                ('pre_rev', models.IntegerField(default=0)),
                ('next_rev', models.IntegerField(default=0)),
                ('posted', models.DateTimeField(verbose_name='date published')),
                ('viewed', models.IntegerField(default=0)),
                ('downloaded', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('policy_cc', models.BooleanField(default=False)),
                ('policy_adaptations', models.CharField(max_length=30)),
                ('policy_commercial', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mod',
            },
        ),
        migrations.CreateModel(
            name='Palettes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=400)),
                ('used', models.IntegerField(default=0)),
                ('posted', models.DateTimeField(verbose_name='date published')),
                ('rating', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Palette',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_id', models.IntegerField(default=0)),
                ('ex_name', models.CharField(max_length=16)),
                ('rating', models.FloatField(default=0.0)),
                ('posted', models.DateTimeField(verbose_name='date rated')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rating',
            },
        ),
        migrations.CreateModel(
            name='ReplayPlayers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('replay_id', models.IntegerField(default=0)),
                ('client_index', models.IntegerField(default=0)),
                ('color', models.CharField(max_length=30)),
                ('faction_id', models.CharField(max_length=50)),
                ('faction_name', models.CharField(max_length=50)),
                ('is_bot', models.BooleanField(default=False)),
                ('is_human', models.BooleanField(default=True)),
                ('is_random_faction', models.BooleanField(default=False)),
                ('is_random_spawn', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000)),
                ('outcome', models.CharField(max_length=50)),
                ('outcome_timestamp', models.CharField(max_length=50)),
                ('spawn_point', models.IntegerField(default=0)),
                ('team', models.IntegerField(default=0)),
                ('posted', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ReplayPlayer',
            },
        ),
        migrations.CreateModel(
            name='Replays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(default='', max_length=2000)),
                ('metadata', models.CharField(default='', max_length=100000)),
                ('game_mod', models.CharField(default='', max_length=100)),
                ('map_hash', models.CharField(default='', max_length=200)),
                ('version', models.CharField(default='release-20141029', max_length=100)),
                ('start_time', models.CharField(default='', max_length=50)),
                ('end_time', models.CharField(default='', max_length=50)),
                ('sha1sum', models.CharField(default='', max_length=200)),
                ('parser', models.CharField(default='release-20141029', max_length=100)),
                ('posted', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
                ('viewed', models.IntegerField(default=0)),
                ('downloaded', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Replay',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=400)),
                ('ex_id', models.IntegerField(default=0)),
                ('ex_name', models.CharField(max_length=16)),
                ('infringement', models.BooleanField(default=False)),
                ('posted', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Report',
            },
        ),
        migrations.CreateModel(
            name='Screenshots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ex_id', models.IntegerField(default=0)),
                ('ex_name', models.CharField(max_length=16)),
                ('posted', models.DateTimeField(verbose_name='date published')),
                ('map_preview', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Screenshot',
            },
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=400)),
                ('unit_type', models.CharField(max_length=16)),
                ('category', models.CharField(max_length=16)),
                ('palette', models.CharField(max_length=16)),
                ('revision', models.IntegerField(default=1)),
                ('pre_rev', models.IntegerField(default=0)),
                ('next_rev', models.IntegerField(default=0)),
                ('posted', models.DateTimeField(verbose_name='date published')),
                ('viewed', models.IntegerField(default=0)),
                ('downloaded', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('policy_cc', models.BooleanField(default=False)),
                ('policy_adaptations', models.CharField(max_length=30)),
                ('policy_commercial', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Unit',
            },
        ),
        migrations.CreateModel(
            name='UnsubscribeComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(default='maps', max_length=16)),
                ('item_id', models.IntegerField(default=0)),
                ('unsubscribed', models.DateTimeField(verbose_name='date of unsubscribe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UnsubscribeComment',
            },
        ),
    ]
