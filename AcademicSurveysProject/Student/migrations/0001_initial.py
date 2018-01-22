# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=30, unique=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('primary_email', models.EmailField(max_length=100)),
                ('secondary_email', models.EmailField(max_length=100)),
                ('type', models.CharField(choices=[('fr', 'Fresh'), ('ot', 'Other')], default='fr', max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]