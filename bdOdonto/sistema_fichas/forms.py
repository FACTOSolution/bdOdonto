#coding: latin-1
from django import forms

from .models import *

class Ficha_UrgenciaForm(forms.ModelForm):

    class Meta:
        model = Ficha_Urgencia
        fields = ('História Clínica (condições de saúde)', 'Medicamentos em uso no momento', 'Motivo da consulta', 'Diagnóstico provável após anamnese', 'Atendimento', 'Encaminhamento ou reagendamento', 'Prescrições Medicamentosas', 'Especialidade em que se enquadrou o atendimento de urgência')

class Ficha_PPRForm(forms.ModelForm):

    class Meta:
        model = Ficha_PPR
        fields = ('Classificação de Kennedy (superior)', 
        	'Tratamento prévio (superior)', 
        	'Planejamento da Prótese Removível: Apoios: tipo e localização, retentores, conector maior, sela. (superior)', 
        	'Observações (superior)',
        	'Classificação de Kennedy (inferior)', 
        	'Tratamento prévio (inferior)',
        	'Planejamento da Prótese Removível: Apoios: tipo e localização, retentores, conector maior, sela. (inferior)', 
        	'Observações (inferior)'
        	)
