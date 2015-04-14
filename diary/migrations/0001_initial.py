# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0014_auto_20150315_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hw_date', models.DateField()),
                ('hw_descr', models.CharField(max_length=200)),
                ('lesson', models.ForeignKey(to='timetable.Lessons')),
            ],
            options={
                'ordering': ['hw_date'],
            },
        ),
    ]
