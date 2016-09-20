# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0007_auto_20160830_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_product',
            name='statue',
            field=models.IntegerField(default=0, verbose_name='商品状态', editable=False),
        ),
    ]
