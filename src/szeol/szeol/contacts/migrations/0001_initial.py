# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import szeol.main.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nazwa', max_length=50)),
                ('surname', models.CharField(help_text='Surname', max_length=50)),
                ('address', models.CharField(help_text='Address', max_length=255)),
                ('when_created', models.DateTimeField(db_index=True, default=szeol.main.utils.default_now)),
            ],
        ),
    ]
