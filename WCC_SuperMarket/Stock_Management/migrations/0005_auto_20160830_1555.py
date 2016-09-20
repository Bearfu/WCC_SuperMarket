# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0004_mall_order_statue'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_product',
            name='size',
            field=models.IntegerField(verbose_name='条码大小', default=True),
        ),
        migrations.AddField(
            model_name='mall_in_product_log',
            name='operating',
            field=models.IntegerField(verbose_name='进货操作， 0：进货，1：打印', default=True),
        ),
        migrations.AddField(
            model_name='mall_out_product',
            name='activity',
            field=models.TextField(verbose_name='参与何种活动', default=True),
        ),
        migrations.AddField(
            model_name='mall_out_product',
            name='all_price',
            field=models.FloatField(verbose_name='合计金额', default=True),
        ),
        migrations.AddField(
            model_name='mall_out_product',
            name='in_come',
            field=models.FloatField(verbose_name='收到金额', default=True),
        ),
        migrations.AddField(
            model_name='mall_out_product',
            name='off_price',
            field=models.FloatField(verbose_name='优惠金额', default=True),
        ),
        migrations.AddField(
            model_name='mall_out_product',
            name='out_come',
            field=models.FloatField(verbose_name='找零金额', default=True),
        ),
        migrations.AddField(
            model_name='mall_out_product',
            name='statue',
            field=models.IntegerField(verbose_name='订单状态，0：未支付，1：已支付', default=True),
        ),
    ]
