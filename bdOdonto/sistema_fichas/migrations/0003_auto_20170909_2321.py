# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-10 02:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_fichas', '0002_auto_20170909_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='turma_Aluno',
            new_name='turma_aluno',
        ),
        migrations.RenameField(
            model_name='paciente',
            old_name='turma_Aluno',
            new_name='turma_aluno',
        ),
    ]
