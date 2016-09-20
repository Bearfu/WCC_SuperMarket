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
                ('productID', models.AutoField(verbose_name='商品店内ID', primary_key=True, serialize=False)),
                ('barcode', models.BigIntegerField(verbose_name='商品条码', default=True, db_index=True)),
                ('product_name', models.CharField(verbose_name='商品名称', default=True, db_index=True, max_length=128)),
                ('in_price', models.FloatField(verbose_name='进货价格', default=True)),
                ('spec', models.CharField(verbose_name='商品规格', default=True, max_length=50)),
                ('unit', models.CharField(verbose_name='商品包装', default=True, max_length=50)),
                ('source', models.CharField(verbose_name='供应商', default=True, max_length=50)),
                ('big_class', models.CharField(verbose_name='商品分类（一级）', default=True, max_length=50)),
                ('small_class', models.CharField(verbose_name='商品分类（二级）', default=True, max_length=50)),
                ('storage_methods', models.CharField(verbose_name='存放方式', default=True, max_length=50)),
                ('shelf_life', models.IntegerField(verbose_name='保质期', default=True)),
                ('discount', models.CharField(verbose_name='折扣', default=True, max_length=50)),
                ('activity', models.IntegerField(verbose_name='是否参加活动', default=True)),
                ('stock', models.IntegerField(verbose_name='库存', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='mall_in_product',
            fields=[
                ('in_productID', models.AutoField(verbose_name='进货批次ID', primary_key=True, serialize=False)),
                ('barcode', models.BigIntegerField(verbose_name='商品条码', db_index=True)),
                ('in_price', models.FloatField(verbose_name='进货价格', default=True)),
                ('num', models.IntegerField(verbose_name='进货数量')),
                ('in_datetime', models.DateTimeField(verbose_name='进货时间')),
                ('batch', models.CharField(verbose_name='进货批次号', max_length=15)),
                ('source', models.CharField(verbose_name='进货渠道', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='mall_in_product_log',
            fields=[
                ('in_productID', models.AutoField(verbose_name='进货LOG_ID', primary_key=True, serialize=False)),
                ('barcode', models.BigIntegerField(verbose_name='商品条码', db_index=True)),
                ('rainbow_code', models.BigIntegerField(verbose_name='彩虹码', db_index=True)),
                ('in_price', models.FloatField(verbose_name='进货价格', default=True)),
                ('in_datetime', models.DateTimeField(verbose_name='进货时间', default=True)),
                ('batch', models.CharField(verbose_name='进货批次号', default=True, max_length=15)),
                ('source', models.CharField(verbose_name='进货渠道', default=True, max_length=15)),
                ('device_id', models.IntegerField(verbose_name='打印机编号', default=True)),
                ('operator', models.IntegerField(verbose_name='操作员', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='mall_order',
            fields=[
                ('ID', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('orderID', models.CharField(verbose_name='订单编号', default=True, max_length=15)),
                ('barcode', models.TextField(verbose_name='商品条码(列表)', default=True)),
                ('num_price', models.FloatField(verbose_name='合计金额', default=True)),
                ('off_price', models.FloatField(verbose_name='优惠金额', default=True)),
                ('in_come', models.FloatField(verbose_name='收到金额', default=True)),
                ('out_come', models.FloatField(verbose_name='找零金额', default=True)),
                ('activity', models.TextField(verbose_name='参与何种活动', default=True)),
                ('out_datetime', models.DateTimeField(verbose_name='订单生成时间', default=True)),
                ('operator_num', models.CharField(verbose_name='操作员工号', default=True, max_length=15)),
                ('pos_num', models.CharField(verbose_name='收银机编号', default=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='mall_out_product',
            fields=[
                ('in_productID', models.AutoField(verbose_name='出货批次ID', primary_key=True, serialize=False)),
                ('barcode', models.BigIntegerField(verbose_name='商品条码', db_index=True)),
                ('rainbow_code', models.BigIntegerField(verbose_name='商品彩虹码', db_index=True)),
                ('orderID', models.CharField(verbose_name='订单编号', max_length=15)),
                ('out_price', models.FloatField(verbose_name='卖出价格')),
                ('out_datetime', models.DateTimeField(verbose_name='进货时间')),
                ('operator_num', models.CharField(verbose_name='操作员工号', max_length=15)),
                ('pos_num', models.CharField(verbose_name='收银机编号', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='rainbow_code_table',
            fields=[
                ('ID', models.AutoField(verbose_name='彩虹码ID', primary_key=True, serialize=False)),
                ('barcode', models.BigIntegerField(verbose_name='商品条码', default=True, db_index=True)),
                ('rainbow_code', models.BigIntegerField(verbose_name='彩虹码', default=True, db_index=True)),
                ('in_price', models.FloatField(verbose_name='进货价格', default=True)),
                ('out_price', models.FloatField(verbose_name='定价', default=True)),
                ('batch', models.CharField(verbose_name='进货批次', max_length=15)),
                ('create_time', models.DateTimeField(verbose_name='彩虹码生成时间', auto_now_add=True)),
                ('use_time', models.DateTimeField(verbose_name='彩虹码使用时间', auto_now_add=True)),
                ('production_date', models.DateTimeField(verbose_name='商品生产日期', auto_now_add=True)),
                ('end_date', models.DateTimeField(verbose_name='商品过期日期', auto_now_add=True)),
                ('discount', models.IntegerField(verbose_name='折扣', default=True)),
                ('activity', models.IntegerField(verbose_name='是否参加活动', default=True)),
                ('statue', models.IntegerField(verbose_name='商品状态', default=True)),
                ('print_times', models.IntegerField(verbose_name='打印次数', default=True)),
                ('code_statue', models.IntegerField(verbose_name='彩虹码状态', default=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rainbow_code_table',
            unique_together=set([('barcode', 'rainbow_code')]),
        ),
    ]
