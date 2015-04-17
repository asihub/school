# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galery', '0004_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='galery/photo/', verbose_name='Фотографія')),
                ('description', models.CharField(max_length=200, verbose_name='Коментар', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('galery', models.ForeignKey(to='galery.Galery', verbose_name='Альбом')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='album',
        ),
        migrations.RemoveField(
            model_name='album',
            name='user',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
