# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gongfubrew',
            old_name='tea_name',
            new_name='tea',
        ),
        migrations.AddField(
            model_name='gongfubrew',
            name='brew_name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='westernbrew',
            name='brew_name',
            field=models.CharField(default='default name', max_length=100),
            preserve_default=False,
        ),
    ]
