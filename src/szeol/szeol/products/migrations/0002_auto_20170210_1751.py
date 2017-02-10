# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import szeol.main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='when_created',
            field=models.DateTimeField(db_index=True, default=szeol.main.utils.default_now),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('wh', 'Białe'), ('re', 'Czerwone'), ('ro', 'Różowe')], help_text='Kolor', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Nazwa', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='taste',
            field=models.CharField(choices=[('d', 'Wytrawne'), ('sd', 'Półwytrawne'), ('ss', 'Półsłodkie'), ('s', 'Słodkie')], help_text='Smak', max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='year',
            field=models.CharField(help_text='Rocznik', max_length=5),
        ),
    ]
