# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-21 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='users',
        ),
        migrations.AddField(
            model_name='quote',
            name='joiner',
            field=models.ManyToManyField(related_name='joiner', to='app.User'),
        ),
    ]
