# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-30 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funstar', '0003_auto_20180530_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='funstar.Profile'),
        ),
    ]
