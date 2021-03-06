# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-02 06:10
# flake8: noqa
from __future__ import unicode_literals

import clublink.base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0042_auto_20170802_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubadvertisement',
            name='image',
            field=models.ImageField(upload_to=clublink.base.utils.RandomizedUploadPath('sponsors/club/image/')),
        ),
        migrations.AlterField(
            model_name='clubadvertisement',
            name='sort',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='clubadvertisement',
            name='thumbnail',
            field=models.ImageField(upload_to=clublink.base.utils.RandomizedUploadPath('sponsors/club/thumbnail/')),
        ),
        migrations.AlterField(
            model_name='clubadvertisement',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='corpadvertisement',
            name='image',
            field=models.ImageField(upload_to=clublink.base.utils.RandomizedUploadPath('sponsors/corp/image/')),
        ),
        migrations.AlterField(
            model_name='corpadvertisement',
            name='sort',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='corpadvertisement',
            name='thumbnail',
            field=models.ImageField(upload_to=clublink.base.utils.RandomizedUploadPath('sponsors/corp/thumbnail/')),
        ),
        migrations.AlterField(
            model_name='corpadvertisement',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
