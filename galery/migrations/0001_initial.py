# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Galery',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Назва альбому', max_length=200)),
                ('description', models.CharField(blank=True, verbose_name='Опис', max_length=200)),
                ('status', models.IntegerField(choices=[(0, 'Відключений'), (1, 'Загальний'), (2, 'Тільки для користувачів')], default=2, verbose_name='Статус')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
