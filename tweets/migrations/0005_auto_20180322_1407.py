# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_twee_t_hashtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twee_t',
            old_name='hashtag',
            new_name='Hashtag',
        ),
        migrations.RenameField(
            model_name='twee_t',
            old_name='timestamp',
            new_name='Timestamp',
        ),
        migrations.RenameField(
            model_name='twee_t',
            old_name='tweet_content',
            new_name='Tweet_content',
        ),
        migrations.RenameField(
            model_name='twee_t',
            old_name='updated',
            new_name='Updated',
        ),
        migrations.RenameField(
            model_name='twee_t',
            old_name='user',
            new_name='User',
        ),
        migrations.AddField(
            model_name='twee_t',
            name='City_name',
            field=models.CharField(default='Patna', max_length=20),
        ),
        migrations.AddField(
            model_name='twee_t',
            name='College_name',
            field=models.CharField(default='Institute if engineering and management', max_length=200),
        ),
        migrations.AddField(
            model_name='twee_t',
            name='Phone',
            field=models.IntegerField(default=7004602281),
        ),
        migrations.AddField(
            model_name='twee_t',
            name='State',
            field=models.CharField(default='Bihar', max_length=20),
        ),
    ]