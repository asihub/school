# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_timetable_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='dayOfWeek',
            field=models.CharField(choices=[('Понеділок', 'Понеділок'), ('Вівторок', 'Вівторок'), ('Середа', 'Середа'), ('Четвер', 'Четвер'), ('ятниця', "П'ятниця"), ('Субота', 'Субота')], default='Mo', max_length=10),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='lesson',
            field=models.CharField(choices=[('Інформатика', 'Інформатика'), ('Історія України', 'Історія України'), ('Англійська мова', 'Англійська мова'), ('Біологія', 'Біологія'), ('Виховна', 'Виховна'), ('Географія', 'Географія'), ('Логіка', 'Логіка'), ('Малювання', 'Малювання'), ('Математика', 'Математика'), ('Музика', 'Музика'), ('Німецька мова', 'Німецька мова'), ("Основи здоров'я", "Основи здоров'я"), ('Праця', 'Праця'), ('Світова література', 'Світова література'), ('Українська література', 'Українська література'), ('Українська мова', 'Українська мова'), ('Фізкультура', 'Фізкультура')], default='English', max_length=30),
        ),
    ]
