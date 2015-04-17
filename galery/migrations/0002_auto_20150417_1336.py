# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='photo',
            name='thumbnail_path',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='photo',
            name='thumbnail_url',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
