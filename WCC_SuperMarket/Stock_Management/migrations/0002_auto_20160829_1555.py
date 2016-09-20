# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='mall_out_product',
            unique_together=set([('barcode', 'rainbow_code')]),
        ),
    ]
