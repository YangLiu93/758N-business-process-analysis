# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-15 21:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20170415_0635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='return_order',
            name='ProdOrderId',
        ),
        migrations.AddField(
            model_name='return_order',
            name='ProductId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.ProductOrder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='return_order',
            name='ProductName',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
