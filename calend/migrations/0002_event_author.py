# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.CharField(default=datetime.datetime(2015, 4, 8, 9, 52, 40, 576445, tzinfo=utc), max_length=40, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
