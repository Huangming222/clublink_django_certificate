# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-17 06:23
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def set_signature(apps, schema_editor):
    EmailSignature = apps.get_model('certificates', 'EmailSignature')
    CertificateBatch = apps.get_model('certificates', 'CertificateBatch')

    for b in CertificateBatch.objects.all():
        try:
            e = EmailSignature.objects.get(name=b.email_signature)
        except EmailSignature.DoesNotExist:
            e = EmailSignature.objects.first()
        b.email_signature_new = e
        b.save()


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0048_auto_20170413_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatebatch',
            name='email_signature_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='certificates.EmailSignature'),
        ),
        migrations.RunPython(set_signature),
    ]