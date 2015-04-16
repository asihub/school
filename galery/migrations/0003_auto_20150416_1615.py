# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0002_auto_20150416_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galery',
            old_name='album',
            new_name='title',
        ),
    ]
