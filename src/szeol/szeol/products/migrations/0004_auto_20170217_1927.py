# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Price', max_digits=10),
        ),
    ]
