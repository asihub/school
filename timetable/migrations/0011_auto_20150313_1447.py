# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0010_auto_20150313_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaysOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayNum', models.IntegerField()),
                ('dayName', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='timetable',
            name='dayOfWeek',
            field=models.ForeignKey(to='timetable.DaysOfWeek'),
        ),
    ]
