# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20150312_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='room',
            field=models.CharField(max_length=2),
        ),
    ]