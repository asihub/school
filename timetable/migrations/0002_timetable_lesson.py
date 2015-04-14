# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='lesson',
            field=models.CharField(choices=[('Informathics', 'Інформатика'), ('History of UA', 'Історія України'), ('English', 'Англійська мова'), ('Biology', 'Біологія'), ('Educational', 'Виховна'), ('Geography', 'Географія'), ('Logic', 'Логіка'), ('Drawing', 'Малювання'), ('Math', 'Математика'), ('Music', 'Музика'), ('Deutch', 'Німецька мова'), ('Health', "Основи здоров'я"), ('Work', 'Праця'), ('World Literature', ' Світова література'), ('Ukrainian Literature', 'Українська література'), ('Ukrainian Lang', 'Українська мова'), ('Phisician', 'Фізкультура')], default='English', max_length=30),
        ),
    ]
