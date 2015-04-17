# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galery', '0006_auto_20150417_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='galery',
            field=models.ForeignKey(default=datetime.datetime(2015, 4, 17, 7, 4, 46, 848855, tzinfo=utc), to='galery.Galery', verbose_name='Альбом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='timestamp',
            field=models.DateTimeField(verbose_name='Добавлено', default=datetime.datetime(2015, 4, 17, 7, 5, 9, 893203, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
