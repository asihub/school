# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='hw_date',
            field=models.DateField(verbose_name='На котрий день'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='hw_descr',
            field=models.CharField(max_length=200, verbose_name='Завдання'),
        ),
    ]
