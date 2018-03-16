# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-16 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_remove_twee_t_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='twee_t',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
