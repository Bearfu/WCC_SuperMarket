# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0013_auto_20160901_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='rainbow_code_table',
            name='off_price',
            field=models.FloatField(verbose_name='优惠金额', editable=False, default=0),
        ),
        migrations.AlterField(
            model_name='rainbow_code_table',
            name='in_price',
            field=models.FloatField(verbose_name='进货价格', editable=False, default=0),
        ),
        migrations.AlterField(
            model_name='rainbow_code_table',
            name='out_price',
            field=models.FloatField(verbose_name='定价', editable=False, default=0),
        ),
    ]
