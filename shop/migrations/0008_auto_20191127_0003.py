# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-11-27 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20191126_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='available',
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='shop.Category'),
        ),
        migrations.AlterField(
            model_name='student',
            name='document',
            field=pyuploadcare.dj.models.FileField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='perfomance_card',
            field=pyuploadcare.dj.models.FileField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=pyuploadcare.dj.models.ImageField(blank=True, null=True),
        ),
    ]