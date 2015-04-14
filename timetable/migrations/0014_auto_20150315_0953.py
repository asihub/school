# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0013_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='lesson',
            field=models.ForeignKey(to='timetable.Lessons'),
        ),
    ]
