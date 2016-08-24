# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='m_product',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False, verbose_name='商品店内ID')),
                ('barcode', models.BigIntegerField(db_index=True, default=True, verbose_name='商品条码')),
                ('product_name', models.CharField(max_length=128, db_index=True, default=True, verbose_name='商品名称')),
                ('in_price', models.FloatField(default=True, verbose_name='进货价格')),
                ('spec', models.CharField(max_length=50, default=True, verbose_name='商品规格')),
                ('unit', models.CharField(max_length=50, default=True, verbose_name='商品包装')),
                ('source', models.CharField(max_length=50, default=True, verbose_name='供应商')),
                ('big_class', models.CharField(max_length=50, default=True, verbose_name='商品分类（一级）')),
                ('small_class', models.CharField(max_length=50, default=True, verbose_name='商品分类（二级）')),
                ('storage_methods', models.CharField(max_length=50, default=True, verbose_name='存放方式')),
                ('shelf_life', models.IntegerField(default=True, verbose_name='保质期')),
                ('discount', models.CharField(max_length=50, default=True, verbose_name='折扣')),
                ('activity', models.IntegerField(default=True, verbose_name='是否参加活动')),
                ('stock', models.IntegerField(default=True, verbose_name='库存')),
            ],
        ),
        migrations.CreateModel(
            name='rainbow_code_table',
            fields=[
                ('ID', models.IntegerField(auto_created=True, serialize=False, primary_key=True, verbose_name='彩虹码ID')),
                ('barcode', models.BigIntegerField(db_index=True, verbose_name='商品条码')),
                ('rainbow_code', models.BigIntegerField(db_index=True, verbose_name='彩虹码')),
                ('in_price', models.FloatField(default=True, verbose_name='进货价格')),
                ('out_price', models.FloatField(default=True, verbose_name='定价')),
                ('batch', models.CharField(max_length=15, verbose_name='进货批次')),
                ('create_time', models.DateTimeField(verbose_name='彩虹码生成时间')),
                ('use_time', models.DateTimeField(verbose_name='彩虹码使用时间')),
                ('production_date', models.DateTimeField(verbose_name='商品生产日期')),
                ('end_date', models.DateTimeField(verbose_name='商品过期日期')),
                ('discount', models.IntegerField(verbose_name='折扣')),
                ('activity', models.IntegerField(verbose_name='是否参加活动')),
                ('statue', models.IntegerField(verbose_name='商品状态')),
            ],
        ),
    ]
