# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-17 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0007_auto_20180417_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={},
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='timestamp',
            new_name='created_data',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='updated',
            new_name='updated_data',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='content',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='width_field',
        ),
        migrations.AddField(
            model_name='goal',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goal',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
