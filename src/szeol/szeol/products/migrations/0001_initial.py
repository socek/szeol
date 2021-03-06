# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=5)),
                ('taste', models.CharField(choices=[('d', 'Dry'), ('sd', 'Semi-Dry'), ('ss', 'Semi-Sweet'), ('s', 'Sweet')], max_length=2)),
                ('color', models.CharField(choices=[('wh', 'White'), ('re', 'Red'), ('ro', 'Rosé')], max_length=2)),
            ],
        ),
    ]
