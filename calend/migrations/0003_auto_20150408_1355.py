# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calend', '0002_event_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ev_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 8, 10, 55, 9, 363664, tzinfo=utc), verbose_name='Час проведення'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='ev_time',
            field=models.TimeField(verbose_name='Час проведення'),
        ),
    ]
