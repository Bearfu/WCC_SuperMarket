# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0010_m_product_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_product',
            name='level',
            field=models.CharField(max_length=50, default=True, verbose_name='商品等级'),
        ),
        migrations.AddField(
            model_name='m_product_test',
            name='level',
            field=models.CharField(max_length=50, default=True, verbose_name='商品等级'),
        ),
    ]
