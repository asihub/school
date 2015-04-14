# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calend', '0003_auto_20150408_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='body',
        ),
        migrations.AddField(
            model_name='event',
            name='note',
            field=models.TextField(verbose_name='Примітка', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.BooleanField(verbose_name='Статус', choices=[(0, 'Відмінено'), (1, 'Заплановано')], default='1'),
        ),
    ]
