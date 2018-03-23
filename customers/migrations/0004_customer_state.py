# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-04 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20170713_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, choices=[(b'KA', b'Karnataka'), (b'AP', b'Andhra Pradesh'), (b'KL', b'Kerala'), (b'TN', b'Tamil Nadu'), (b'MH', b'Maharashtra'), (b'UP', b'Uttar Pradesh'), (b'GA', b'Goa'), (b'GJ', b'Gujarat'), (b'RJ', b'Rajasthan'), (b'HP', b'Himachal Pradesh'), (b'JK', b'Jammu and Kashmir'), (b'TG', b'Telangana'), (b'AR', b'Arunachal Pradesh'), (b'AS', b'Assam'), (b'BR', b'Bihar'), (b'CG', b'Chattisgarh'), (b'HR', b'Haryana'), (b'JH', b'Jharkhand'), (b'MP', b'Madhya Pradesh'), (b'MN', b'Manipur'), (b'ML', b'Meghalaya'), (b'MZ', b'Mizoram'), (b'NL', b'Nagaland'), (b'OR', b'Orissa'), (b'PB', b'Punjab'), (b'SK', b'Sikkim'), (b'TR', b'Tripura'), (b'UA', b'Uttarakhand'), (b'WB', b'West Bengal'), (b'AN', b'Andaman and Nicobar'), (b'CH', b'Chandigarh'), (b'DN', b'Dadra and Nagar Haveli'), (b'DD', b'Daman and Diu'), (b'DL', b'Delhi'), (b'LD', b'Lakshadweep'), (b'PY', b'Pondicherry')], max_length=2, null=True),
        ),
    ]
