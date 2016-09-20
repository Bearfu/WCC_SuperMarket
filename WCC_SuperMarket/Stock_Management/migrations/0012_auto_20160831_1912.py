# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0011_auto_20160831_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mall_in_product_log',
            name='operator',
            field=models.CharField(default=True, verbose_name='操作员', max_length=15),
        ),
    ]
