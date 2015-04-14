# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_auto_20150313_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='week_parity',
            field=models.CharField(choices=[(0, 'П+Н'), (1, 'Н'), (2, 'П')], default='П+Н', max_length=1),
        ),
    ]
