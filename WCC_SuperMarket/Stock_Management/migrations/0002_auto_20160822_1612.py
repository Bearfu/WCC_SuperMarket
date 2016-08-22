# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock_Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='m_product',
            name='big_class',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='m_product',
            name='small_class',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='m_product',
            name='storage_methods',
            field=models.CharField(default=True, max_length=50),
        ),
    ]
