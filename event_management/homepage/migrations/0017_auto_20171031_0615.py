# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-31 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0016_auto_20171031_0613'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubs',
            name='Blog',
            field=models.CharField(default='', max_length=3200),
        ),
        migrations.AddField(
            model_name='clubs',
            name='Description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='clubs',
            name='Events',
            field=models.CharField(default='', max_length=3200),
        ),
        migrations.AddField(
            model_name='clubs',
            name='Members',
            field=models.CharField(default='', max_length=3200),
        ),
        migrations.AddField(
            model_name='clubs',
            name='interests',
            field=models.CharField(default='', max_length=3200),
        ),
    ]