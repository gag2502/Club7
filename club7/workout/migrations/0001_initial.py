# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout', models.CharField(max_length=1)),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
