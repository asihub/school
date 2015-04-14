# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0014_auto_20150315_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='lesson',
            field=models.CharField(max_length=40, verbose_name='Урок'),
        ),
    ]
