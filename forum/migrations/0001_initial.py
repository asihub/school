# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=60, verbose_name='Розділ')),
                ('description', models.CharField(max_length=200, verbose_name='Опис')),
                ('order', models.IntegerField(verbose_name='Порядок')),
            ],
        ),
    ]
