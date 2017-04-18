# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20170413_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 11, 35, 11, 268010, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 11, 35, 11, 268045, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
