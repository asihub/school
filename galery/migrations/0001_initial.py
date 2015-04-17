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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Назва альбому', max_length=200)),
                ('description', models.CharField(blank=True, verbose_name='Опис', max_length=200)),
                ('status', models.IntegerField(verbose_name='Статус', default=2, choices=[(0, 'Відключений'), (1, 'Загальний'), (2, 'Тільки для користувачів')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('photo', models.ImageField(verbose_name='Фотографія', upload_to='galery/photo/')),
                ('description', models.CharField(blank=True, verbose_name='Коментар', max_length=200)),
                ('timestamp', models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)),
                ('galery', models.ForeignKey(verbose_name='Альбом', to='galery.Galery')),
                ('user', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
