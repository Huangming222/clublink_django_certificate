# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-11-06 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0066_club_teeitup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='code',
            field=models.CharField(max_length=4),
        ),
    ]
