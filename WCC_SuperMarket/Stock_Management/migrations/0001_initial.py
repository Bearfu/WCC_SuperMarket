# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='m_product',
            fields=[
                ('productID', models.AutoField(serialize=False, primary_key=True)),
                ('barcode', models.CharField(db_index=True, max_length=50, default=True)),
                ('product_name', models.CharField(db_index=True, max_length=500, default=True)),
                ('in_price', models.FloatField(default=True)),
                ('out_price', models.FloatField(default=True)),
                ('spec', models.CharField(max_length=50, default=True)),
                ('unit', models.CharField(max_length=50, default=True)),
                ('shelf_life', models.IntegerField(default=True)),
                ('discount', models.CharField(max_length=50, default=True)),
                ('activity', models.CharField(max_length=50, default=True)),
                ('stock', models.IntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='rainbow_code_table',
            fields=[
                ('ID', models.IntegerField(auto_created=True, serialize=False, primary_key=True)),
                ('barcode', models.CharField(db_index=True, max_length=50)),
                ('rainbow_code', models.CharField(db_index=True, max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
                ('use_time', models.DateTimeField()),
                ('production_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('discount', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('activity', models.CharField(max_length=50)),
                ('statue', models.CharField(max_length=50)),
            ],
        ),
    ]
