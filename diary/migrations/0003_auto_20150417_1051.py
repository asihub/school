# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20150315_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='lesson',
            field=models.ForeignKey(verbose_name='Урок', to='timetable.Lessons'),
        ),
    ]
