# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-26 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180426_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
