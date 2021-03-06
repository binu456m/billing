# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 18:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shops', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('vendor_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('tin', models.CharField(blank=True, max_length=128, null=True)),
                ('cst', models.CharField(blank=True, max_length=128, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_vendor_objects', to=settings.AUTH_USER_MODEL)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Shop')),
                ('updater', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_vendor_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-vendor_id',),
                'db_table': 'vendors_vendor',
                'verbose_name': 'vendor',
                'verbose_name_plural': 'vendors',
            },
        ),
    ]
