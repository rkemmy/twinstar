# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-30 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funstar', '0004_auto_20180530_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.TextField(default=True, max_length=200),
        ),
    ]
