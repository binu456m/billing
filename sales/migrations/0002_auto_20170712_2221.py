# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-12 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sale',
            options={'ordering': ('-date_added',), 'verbose_name': 'sale', 'verbose_name_plural': 'sales'},
        ),
        migrations.AlterModelOptions(
            name='saleproduct',
            options={'ordering': ('sale', 'id'), 'verbose_name': 'sale product', 'verbose_name_plural': 'sale products'},
        ),
    ]
