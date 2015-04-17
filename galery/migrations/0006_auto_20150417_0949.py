# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0005_auto_20150417_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='galery',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]
