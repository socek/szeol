# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20170401_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount',
            field=models.DecimalField(decimal_places=3, default=0, help_text='Discount in %', max_digits=10),
        ),
    ]
