# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0002_auto_20160829_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mall_order',
            name='orderID',
            field=models.CharField(verbose_name='订单编号', max_length=15, unique=True, default=True),
        ),
    ]
