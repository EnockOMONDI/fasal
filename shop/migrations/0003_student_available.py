# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-10 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190610_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
