# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-12 22:21
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ('-date_added',), 'verbose_name': 'purchase', 'verbose_name_plural': 'purchases'},
        ),
        migrations.AlterModelOptions(
            name='purchaseproduct',
            options={'ordering': ('purchase', 'id'), 'verbose_name': 'purchase product', 'verbose_name_plural': 'purchase products'},
        ),
        migrations.RenameField(
            model_name='purchase',
            old_name='purchase_order_no',
            new_name='invoice_no',
        ),
        migrations.AddField(
            model_name='purchase',
            name='final_total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
        migrations.AddField(
            model_name='purchase',
            name='other_charges',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))]),
        ),
    ]