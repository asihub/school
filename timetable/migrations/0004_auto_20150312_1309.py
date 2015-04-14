# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0003_auto_20150312_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timetable',
            options={'ordering': ['dayOfWeek', 'lessonNumber', 'lesson']},
        ),
    ]
