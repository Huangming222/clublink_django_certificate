# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-26 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0038_clubevent_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubevent',
            options={'ordering': ('start_date', 'start_time')},
        ),
        migrations.RenameField(
            model_name='clubevent',
            old_name='date',
            new_name='start_date',
        ),
    ]
