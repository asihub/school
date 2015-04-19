# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Відповідь')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Опис')),
                ('status', models.IntegerField(choices=[(0, 'Неактивний'), (1, 'Активний')], default=1, verbose_name='Статус')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='vote',
            field=models.ForeignKey(to='vote.Vote'),
        ),
    ]
