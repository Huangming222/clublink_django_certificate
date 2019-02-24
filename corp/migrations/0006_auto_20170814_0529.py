# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-14 09:29
from __future__ import unicode_literals

from django.db import migrations
from django.utils.text import slugify


def slugify_title(apps, schema_editor):
    News = apps.get_model('corp', 'News')

    for n in News.objects.all():
        n.slug = slugify(n.headline)
        n.save()


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0005_auto_20170814_0432'),
    ]

    operations = [
        migrations.RunPython(slugify_title, lambda x, y: None),
    ]