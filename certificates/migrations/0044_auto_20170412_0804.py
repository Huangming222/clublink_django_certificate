# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-12 08:04
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def migrate_recipient_data(apps, schema_editor):
    Certificate = apps.get_model('certificates', 'Certificate')
    CertificateBatch = apps.get_model('certificates', 'CertificateBatch')
    db_alias = schema_editor.connection.alias

    for b in CertificateBatch.objects.using(db_alias).all():
        c = Certificate.objects.using(db_alias).filter(batch=b).first()

        b.account_name = c.account_name
        b.account_number = c.account_number
        b.department_id = c.department_id
        b.email_signature = c.email_signature
        b.recipient_name = c.recipient_name

        b.save()


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0027_auto_20170406_2306'),
        ('certificates', '0043_certificatetype_redemption_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatebatch',
            name='account_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='certificatebatch',
            name='account_number',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='certificatebatch',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certificate_batches', to='clubs.Department'),
        ),
        migrations.AddField(
            model_name='certificatebatch',
            name='email_signature',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='certificatebatch',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French')], default='en', max_length=2),
        ),
        migrations.AddField(
            model_name='certificatebatch',
            name='recipient_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(migrate_recipient_data),
        migrations.AlterField(
            model_name='certificatebatch',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate_batches', to='clubs.Department'),
        )
    ]
