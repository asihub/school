# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, verbose_name='Автор книги', max_length=60),
        ),
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(verbose_name='Файл', upload_to='library/files/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='library',
            field=models.ForeignKey(verbose_name='Бібліотека', to='library.Library'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.SmallIntegerField(blank=True, verbose_name='Рік', null=True),
        ),
    ]
