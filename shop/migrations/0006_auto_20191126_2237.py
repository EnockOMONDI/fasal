# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-26 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190717_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='brief_description',
            field=models.CharField(db_index=True, max_length=900),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
