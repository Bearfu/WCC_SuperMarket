# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0015_auto_20160905_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='rainbow_code_table',
            name='product_name',
            field=models.CharField(default=True, verbose_name='商品名称', db_index=True, max_length=128),
        ),
    ]
