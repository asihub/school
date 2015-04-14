# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0011_auto_20150313_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='daysofweek',
            options={'ordering': ['dayNum']},
        ),
    ]
