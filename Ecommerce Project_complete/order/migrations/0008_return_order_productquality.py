# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-21 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20170416_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='return_order',
            name='ProductQuality',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
