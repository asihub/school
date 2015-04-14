# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOfWeek', models.CharField(choices=[('Mo', 'Понеділок'), ('Tu', 'Вівторок'), ('We', 'Середа'), ('Th', 'Четвер'), ('Fr', "П'ятниця"), ('Sa', 'Субота')], default='Mo', max_length=10)),
                ('lessonNumber', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], default=0)),
                ('room', models.IntegerField()),
                ('begin_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
