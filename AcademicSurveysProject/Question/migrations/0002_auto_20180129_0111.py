# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-28 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('order',), 'verbose_name': 'question', 'verbose_name_plural': 'questions'},
        ),
    ]
