# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-09 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20180305_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
