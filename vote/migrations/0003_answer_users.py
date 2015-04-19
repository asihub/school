# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0002_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='users',
            field=models.ManyToManyField(through='vote.Result', to=settings.AUTH_USER_MODEL),
        ),
    ]
