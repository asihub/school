# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_auto_20150313_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='week_parity',
            field=models.BooleanField(choices=[(0, 'Парний'), (1, 'Непарний')], default=datetime.datetime(2015, 3, 13, 8, 36, 11, 310600, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
