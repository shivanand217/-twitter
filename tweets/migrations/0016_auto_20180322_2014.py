# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0015_auto_20180322_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twee_t',
            name='college_name',
            field=models.CharField(default='Institute of engineering and management', max_length=200),
        ),
    ]