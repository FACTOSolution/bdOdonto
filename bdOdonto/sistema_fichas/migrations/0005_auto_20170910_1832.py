# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_fichas', '0004_auto_20170910_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_diagnostico',
            name='data',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ficha_diagnostico',
            name='ultima_consulta',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_nasc',
            field=models.DateField(),
        ),
    ]
