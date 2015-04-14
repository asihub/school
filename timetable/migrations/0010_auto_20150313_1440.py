# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0009_auto_20150313_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='dayOfWeek',
            field=models.CharField(choices=[('Понеділок', 'Понеділок'), ('Вівторок', 'Вівторок'), ('Середа', 'Середа'), ('Четвер', 'Четвер'), ("5_П'ятниця", "П'ятниця"), ('Субота', 'Субота')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='week_parity',
            field=models.CharField(choices=[('0', 'П+Н'), ('1', 'Н'), ('2', 'П')], default='П+Н', max_length=1),
        ),
    ]
