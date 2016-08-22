# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='m_user',
            fields=[
                ('user_ID', models.IntegerField(serialize=False, primary_key=True, auto_created=True)),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('customer_num', models.CharField(max_length=50)),
                ('role', models.CharField(db_index=True, max_length=50)),
                ('last_login_IP', models.CharField(max_length=50)),
                ('last_login_time', models.DateTimeField()),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]
