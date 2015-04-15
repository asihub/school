# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=60, verbose_name='Назва')),
                ('author', models.CharField(max_length=60, verbose_name='Автор', blank=True)),
                ('year', models.SmallIntegerField(null=True, blank=True)),
                ('file', models.FileField(upload_to='books')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=60, verbose_name='Назва')),
                ('description', models.CharField(max_length=200, verbose_name='Опис', blank=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(to='library.Library'),
        ),
    ]
