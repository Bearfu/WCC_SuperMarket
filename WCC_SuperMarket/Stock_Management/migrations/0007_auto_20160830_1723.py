# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0006_m_product_statue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_product',
            name='statue',
            field=models.IntegerField(verbose_name='商品状态', default=0),
        ),
    ]
