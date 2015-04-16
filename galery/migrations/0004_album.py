# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galery', '0003_auto_20150416_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('photo', models.ImageField(verbose_name='Фотографія', upload_to='galery/photo/')),
                ('description', models.CharField(verbose_name='Коментар', max_length=200, blank=True)),
                ('timestamp', models.DateTimeField(verbose_name='Добавлено', auto_now_add=True)),
                ('album', models.ForeignKey(verbose_name='Альбом', to='galery.Galery')),
                ('user', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
