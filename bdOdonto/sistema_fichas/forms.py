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

class Ficha_PeriodontiaForm(forms.ModelForm):
    
    class Meta:
        model = Ficha_Periodontia
        fields = ('Suas gengivas sangram quando escova os dentes?',
            'Já fez tratamento de gengiva alguma vez?',
            'Já utilizou aparelho ortodôntico?',
            'É alérgico ou tem reações alérgicas a:\nAnestesia dentária',
            'Penicilina ou outros antibióticos',
            'Sulfas',
            'Aspirina',
            'Outros',
            'É alérgico a outra substância que não sejam medicamentos?',
            'Qual(is)',
            'Está atualmente sob cuidados médicos?',
            'Qual motivo?',
            'Está tomando algum medicamento no momento?',
            'Qual(is)',
            'Quais das seguintes enfermidades você tem ou já teve?\nFebre Reumática',
            'Doenças cardiovasculares',
            'Você ou parente tem diabetes?',
            'Tem tonturas de vez em quando?',
            'Já foi alguma vez tratado de anemia?',
            'Esteve acamado por longo tempo nos últimos 5 meses?',
            'Suas juntas doem ou incham com frequência?',
            'Já teve úlcera no estômago ou duodeno?',
            'Tem algum problema com o fígado ou vesícula?',
            'Já teve ou viveu com alguém que tivesse tuberculose?',
            'Quando você se corta a ferida sangra muito?',
            'Sofreu alguma operação nos últimos 5 anos?',
            'Qual?',
            'Sofreu variação de peso ultimamente?',
            'Já fez algum tratamento radioterápico?',
            'Qual região?',
            'Por quanto tempo?',
            'Tem problemas com pressão arterial?',
            'Tem ou teve algum problema associado à sua menstruação?',
            'Está grávida?',
            'É fumante ou ex-fumante?',
            'Há quanto tempo?',
            'QUantos cig/dia?',
            'É portador de alguma doença infecto-contagiosa?',
            'Qual(is)',
            'É ou já foi usuário de drogas ilícitas?',
            )

class Ficha_EndodontiaForm(forms.ModelForm):

    class Meta:
        model = Ficha_Endodontia
        fields = (
            'Está em tratamento médico?',
            'Há quanto tempo?',
            'Tem Diabetes?',
            'Febre reumática?',
            'Alterações Sanguíneas?',
            'Doença cárdio-vascular?',
            'Problemas hemorrágicos?',
            'Hipertensão',
            'É portador de marcapasso?',
            'Está grávida?',
            'De quantos meses?',
            'Já teve hepatite?',
            'Há quanto tempo?',
            'Tipo:',
            'Faz uso de algum medicamento?',
            'Tem alergia?',
            'Outras informações sobre sua saúde',
            'História Dental',
            'Características da dor:',
            'Uso de medicamentos:\nAnalgésicos',
            'Antiinflamatórios',
            'Antibiótico',
            'Dente',
            'Dor exarcebada por:\nFrio',
            'Calor',
            'Percussão horizontal',
            'Palpação Apical',
            'Câmara pulpar:\nNormal',
            'Calcificada',
            'Com perfuração',
            'Com reabsorção interna',
            'Canal radicular:\nAmplo',
            'Atresiado',
            'Já manipulado',
            'Obturação deficiente',
            'Rizogênese incompleta',
            'Instrumento fraturado',
            'Fratura radicular',
            'Sobre-obturação',
            'Reabsorção apical',
            'Reabsorção externa',
            'Reabsorção interna',
            'Perfuração',
            'Pericemento:\nNormal',
            'Espessado',
            'Hipercementose',
            'Periápice:\nOsteíte rarefaciente difusa',
            'Osteíte rarefaciente circunscrita'
            )

class Ficha_OrtodontiaForm(forms.ModelForm):

    class Meta:
        model = Ficha_Ortodontia
        fields = (
            'Queixa principal',
            'Cor da pele',
            'Doenças',
            'Alergias',
            'Quais alergias?',
            'Operação',
            'Estado geral de saúde',
            'Traumatismo em dentes',
            'Tem vontade de corrigir?',
            'Já usou aparelho antes?',
            'Observações',
            'Tipo psicológico',
            'Simetria',
            'Tipo facial',
            'Selamento Facial',
            'Relação Ls/ls em repouso',
            'Espessura labial',
            'Tonicidade labial',
            'Presença de zigomático',
            'Observações',
            'Simetria do sorriso',
            'Quantidade de gengiva e incisivos',
            'Corredor Bucal',
            'Observações',
            'Perfil',
            'Dimensão vertical',
            'Nariz',
            'Selamento labial',
            'Maxila',
            'Presença do zigomático',
            'Ângulo nasolabial',
            'Mandíbula',
            'Quantidade de mento',
            'Posição do lábio inferior',
            'Sulco mentolabial',
            'Observações',
            'Respiração',
            'Deglutição',
            'Fonação',
            'Hábitos',
            'ATM',
            'Observações',
            'Dentatura',
            'Erupção dentária',
            'Arco superior',
            'Arco inferior',
            'Linha média superior',
            'Linha média inferior',
            'Trespasse horizontal',
            'Trespasse vertical',
            'Mordida cruzada',
            'Curva de Spee superior',
            'Curva de Spee inferior',
            'Relação Caninos (dir)',
            'Relação Caninos (esq)',
            'Relação molares (dir)',
            'Relação molares (esq)',
            'Classificação de Angle',
            'Classificação de Andrews',
            'Diagnóstico',
            'Observações',
            'Observações'
            )