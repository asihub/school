# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Міроприємство')),
                ('body', models.TextField(verbose_name='Опис')),
                ('ev_time', models.DateTimeField(verbose_name='Час проведення')),
                ('place', models.CharField(max_length=150, verbose_name='Місце проведення')),
                ('status', models.BooleanField(verbose_name='Статус', choices=[(0, 'Відмінено'), (1, 'Заплановано')])),
            ],
            options={
                'ordering': ['ev_time'],
            },
        ),
    ]
