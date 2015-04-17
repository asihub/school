# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0002_auto_20150417_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail_path',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail_url',
        ),
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
