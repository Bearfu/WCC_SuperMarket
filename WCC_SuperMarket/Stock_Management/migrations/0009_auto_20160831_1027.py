# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0008_auto_20160830_1725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='m_product',
            old_name='statue',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='mall_out_product',
            old_name='statue',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='rainbow_code_table',
            old_name='code_statue',
            new_name='code_status',
        ),
        migrations.RenameField(
            model_name='rainbow_code_table',
            old_name='statue',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='mall_order',
            name='statue',
        ),
        migrations.AddField(
            model_name='m_product',
            name='upload_status',
            field=models.IntegerField(verbose_name='同步状态', default=0, editable=False),
        ),
        migrations.AddField(
            model_name='mall_order',
            name='status',
            field=models.IntegerField(default=True, verbose_name='订单状态，0：未支付，1：已支付,2:已经取消，-1：订单内商品已损坏'),
        ),
        migrations.AddField(
            model_name='mall_order',
            name='upload_status',
            field=models.IntegerField(verbose_name='同步状态，0：未同步，1：已支付,2:同步后已修改', default=0, editable=False),
        ),
        migrations.AddField(
            model_name='rainbow_code_table',
            name='upload_status',
            field=models.IntegerField(verbose_name='同步状态', default=0, editable=False),
        ),
    ]
