# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-04 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='tin',
            new_name='gstin',
        ),
    ]
