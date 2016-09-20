# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0012_auto_20160831_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rainbow_code_table',
            name='print_times',
            field=models.IntegerField(default=0, editable=False, verbose_name='打印次数'),
        ),
    ]
