# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171019_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 12, 56, 2, 247611, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 19, 12, 56, 2, 247110, tzinfo=utc)),
        ),
    ]
