# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_fichas', '0005_auto_20170910_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
