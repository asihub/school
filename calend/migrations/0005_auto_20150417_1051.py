# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calend', '0004_auto_20150408_1423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['ev_date']},
        ),
    ]
