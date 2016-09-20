# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0005_auto_20160830_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_product',
            name='statue',
            field=models.IntegerField(verbose_name='商品状态', default=True),
        ),
    ]
