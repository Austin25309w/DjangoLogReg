# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-21 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='password',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
