# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EducationalYear', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalyear',
            name='end_year',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='educationalyear',
            name='start_year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
