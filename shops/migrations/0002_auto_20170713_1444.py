# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 14:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='tin',
            new_name='gstin',
        ),
    ]
