# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-21 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0011_auto_20170221_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]