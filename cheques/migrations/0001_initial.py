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
        ('vendors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('cheque_number', models.CharField(blank=True, max_length=128, null=True)),
                ('name', models.CharField(max_length=128)),
                ('account_number', models.CharField(max_length=128)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('details', models.TextField(blank=True, max_length=256, null=True)),
                ('is_notified', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_cheque_objects', to=settings.AUTH_USER_MODEL)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.Shop')),
                ('updater', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='updater_cheque_objects', to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.Vendor')),
            ],
            options={
                'ordering': ('-date',),
                'db_table': 'cheque',
                'verbose_name': 'cheque',
                'verbose_name_plural': 'cheques',
            },
        ),
    ]