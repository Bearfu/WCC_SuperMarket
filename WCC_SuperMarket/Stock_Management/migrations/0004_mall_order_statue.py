# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0003_auto_20160829_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='mall_order',
            name='statue',
            field=models.IntegerField(default=True, verbose_name='订单状态，0：未支付，1：已支付'),
        ),
    ]
