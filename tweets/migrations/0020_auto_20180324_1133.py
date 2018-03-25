# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-24 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0019_auto_20180324_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twee_t',
            name='hashtag',
            field=models.CharField(default='', max_length=160, validators=[tweets.validators.validate_hashtag]),
        ),
        migrations.AlterField(
            model_name='twee_t',
            name='tweet_content',
            field=models.CharField(default='', max_length=150, validators=[tweets.validators.validate_tweet_content]),
        ),
    ]
