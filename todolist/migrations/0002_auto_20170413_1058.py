# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.SmallIntegerField(default=0, choices=[(0, b'Active'), (1, b'Done')]),
            preserve_default=True,
        ),
    ]
