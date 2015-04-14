# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('body', models.CharField(max_length=600, verbose_name='Опис')),
                ('timestamp', models.DateTimeField(verbose_name='Час створення')),
                ('author', models.CharField(max_length=40, verbose_name='Автор')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Розділ')),
                ('description', models.CharField(max_length=200, verbose_name='Опис')),
                ('order', models.IntegerField(verbose_name='Порядок')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('description', models.CharField(max_length=200, verbose_name='Опис')),
                ('order', models.IntegerField(verbose_name='Порядок')),
                ('timestamp', models.DateTimeField(verbose_name='Час створення')),
                ('author', models.CharField(max_length=40, verbose_name='Автор')),
                ('section', models.ForeignKey(to='forum.Section')),
            ],
        ),
        migrations.DeleteModel(
            name='Sections',
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(to='forum.Topic'),
        ),
    ]
