# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0003_auto_20170413_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 0, 5, 883614, tzinfo=utc), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 0, 5, 883640, tzinfo=utc), auto_now=True)),
                ('how_is_done', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(to='todolist.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 0, 5, 883042, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 13, 13, 0, 5, 883078, tzinfo=utc), auto_now=True),
            preserve_default=True,
        ),
    ]
