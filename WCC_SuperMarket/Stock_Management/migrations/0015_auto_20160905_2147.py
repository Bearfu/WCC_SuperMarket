# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0014_auto_20160902_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mall_order',
            name='orderID',
            field=models.CharField(max_length=30, verbose_name='订单编号', unique=True, default=True),
        ),
        migrations.AlterField(
            model_name='mall_out_product',
            name='orderID',
            field=models.CharField(max_length=30, verbose_name='订单编号'),
        ),
    ]
