# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20150404_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='order',
        ),
    ]
