# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-09 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_remove_tweet_content2'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='content2',
            field=models.TextField(default='content2'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='content3',
            field=models.TextField(default='content3'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='content4',
            field=models.TextField(default='content4'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content1',
            field=models.TextField(default='content1'),
        ),
    ]
