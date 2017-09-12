# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Professor)
admin.site.register(Paciente)
admin.site.register(Atendimento)
admin.site.register(Ficha_Diagnostico)
admin.site.register(Ficha_Ortodontia)
admin.site.register(Ficha_Periodontia)
admin.site.register(Ficha_Urgencia)
admin.site.register(Ficha_Endodontia)
admin.site.register(Ficha_Endodontia_Tabela)
admin.site.register(Ficha_PPR)
admin.site.register(Ficha_Dentistica)
admin.site.register(Tipo_Ficha)
admin.site.register(Turma_Aluno)

