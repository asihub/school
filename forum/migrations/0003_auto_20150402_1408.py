# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150402_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='topic',
            name='order',
            field=models.IntegerField(blank=True, verbose_name='Порядок', null=True),
        ),
    ]
