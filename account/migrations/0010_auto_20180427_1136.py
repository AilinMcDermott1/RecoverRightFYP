# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-27 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20180426_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
