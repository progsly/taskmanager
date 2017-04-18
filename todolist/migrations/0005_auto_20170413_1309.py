# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20170413_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='done',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 9, 18, 201630, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='done',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 9, 18, 201656, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 9, 18, 201076, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 9, 18, 201108, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
