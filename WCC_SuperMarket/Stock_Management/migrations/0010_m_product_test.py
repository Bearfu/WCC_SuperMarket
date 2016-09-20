# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0009_auto_20160831_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='m_product_test',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False, verbose_name='商品店内ID')),
                ('barcode', models.BigIntegerField(default=True, db_index=True, verbose_name='商品条码')),
                ('product_name', models.CharField(default=True, db_index=True, max_length=128, verbose_name='商品名称')),
                ('size', models.IntegerField(default=True, verbose_name='条码大小')),
                ('in_price', models.FloatField(default=True, verbose_name='进货价格')),
                ('spec', models.CharField(default=True, max_length=50, verbose_name='商品规格')),
                ('unit', models.CharField(default=True, max_length=50, verbose_name='商品包装')),
                ('source', models.CharField(default=True, max_length=50, verbose_name='供应商')),
                ('big_class', models.CharField(default=True, max_length=50, verbose_name='商品分类（一级）')),
                ('small_class', models.CharField(default=True, max_length=50, verbose_name='商品分类（二级）')),
                ('storage_methods', models.CharField(default=True, max_length=50, verbose_name='存放方式')),
                ('shelf_life', models.IntegerField(default=True, verbose_name='保质期')),
                ('discount', models.CharField(default=True, max_length=50, verbose_name='折扣')),
                ('activity', models.IntegerField(default=True, verbose_name='是否参加活动')),
                ('stock', models.IntegerField(default=True, verbose_name='库存')),
                ('status', models.IntegerField(default=0, editable=False, verbose_name='商品状态')),
                ('upload_status', models.IntegerField(default=0, editable=False, verbose_name='同步状态')),
            ],
        ),
    ]
