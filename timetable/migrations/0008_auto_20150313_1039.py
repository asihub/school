# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0007_timetable_week_parity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='week_parity',
            field=models.CharField(choices=[(0, 'П+Н'), (1, 'Н'), (0, 'П')], max_length=1),
        ),
    ]
