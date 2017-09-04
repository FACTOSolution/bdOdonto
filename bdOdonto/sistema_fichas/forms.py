#coding: latin-1
from django import forms

from .models import *

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = '__all__'
        labels = {
            'tel': 'Telefone',
            'cel': 'Celular',
            'data_nasc': 'Data de Nascimento',
            }

class Ficha_UrgenciaForm(forms.ModelForm):

    class Meta:
        model = Ficha_Urgencia
        fields = '__all__'
        labels = {
        'historia_clinica':'História Clínica (condições de saúde)',
        'medicamentos':'Medicamentos em uso no momento', 
        'motivo': 'Motivo da consulta', 
        'diagnostico_provavel':'Diagnóstico provável após anamnese', 
        'atend':'Atendimento', 
        'atend_outro':'Outro',
        'procedimento':'Procedimento realizado'
        'encaminhamento':'Encaminhamento ou reagendamento', 
        'prescricoes':'Prescrições Medicamentosas', 
        'especialidade':'Especialidade em que se enquadrou o atendimento de urgência'
        'especialidade_outro':'Outro'
        }

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

class Ficha_DiagnosticoForm(forms.ModelForm):
    
    class Meta():
        model = Ficha_Diagnostico
        fields = (
            'Motivo da consulta',
            'Historia da doenca atual',
            'Ultima consulta',
            'Como voce cuida da higiene da sua boca?',
	    	'Quantas vezes ao dia escova seus dentes?',
	    	'Tem dentes sensiveis ao calor ou frio?',
	    	'Sua gengiva sangra na escovação ou quando usa fio dental?',
	    	'Tem hábito de morder objetos?',
	    	'Já notou alguma mobilidade em seus dentes?',
            'Usa prótese? Que tipo?',
	    	'Tem hábito de ranger ou apertar os dentes?',
	    	'Tem dentes sensiveis ao calor ou frio?',
	    	'Tem dificuldade de abrir a boca na extensão que gostaria? ',
	    	'Quando abre ou fecha a boca, sente algum estalido?',
	    	'Sente que sua boca é seca?',
	    	'Costuma se expor frequentemente ao sol?',
	    	'Teve ou tem o hábito do tabagismo?',
	    	'Tipo de tabagismo:',
	    	'Duração do hábito:',	
	    	'Há quanto tempo abandonou o hábito?',
	    	'Consome bebidas alcoólicas?',
	    	'Com que frequencia consome bebidas alcoólicas?',
	    	'Usa drogas ilícitas?',
	    	'Qual drogas ilícitas você usa?',
			'Está em tratamento médico?',	    	
			'Está tomando alguma medicação no momento?',
	    	'Qual medicação?',
	    	'Já sofreu alguma doença grave?',
			'Já se submeteu a alguma cirurgia?',
			'Qual cirurgia?',
			'Faz uso de anticoncepcional?',
			'Está grávida?',
			'Qual o tempo de gestação?',
			'Tem algum tipo de alergia?',
			'Qual alergia?',
			'Já teve reação a algum medicamento?',
			'Qual medicamento?',
			'Já se submeteu à anestesia dentária?',
			'Teve alguma reação?',
			'Já se submeteu à anestesia geral?',
			'Teve alguma reação?',
			'Tem algum distúrbio respiratório?',
			'Qual distúrbio respiratório?',
			'É hipertenso?',
			'Qual a sua pressão arterial?',
			'Sangra muito quando se corta ou extrai dentes?',
			'Sente o coração bater muito rapidamente?',
			'Sente falta de ar ou cansaço com esforço leve?',
			'Costuma ter pés e pernas inchados?',
			'Teve febre reumática?',
			'Tem ou teve algum problema cardiovascular?',
			'Qual?',
			'Tem ou teve alguma dst(s)?',
			'Qual?',
			'Tem conhecimento de ser portador de algum virus?',
			'Qual?',
			'É diabético?',
			'Quando se fere, a cicatrização demora a ocorrer?',
			'Tem perdido peso recentemente, sem causa aparente?',
			'Percebeu aumento na frequencia com que urina?',
			'Tem desmaios frequentes?',
			'Tem (teve) convulsões?',
			'Tem epilepsia?',
			'É portador de algum disturbio sanguineo?',
			'Qual?',
			'Tem algum outro problema de saúde não citado?',
			'Qual?',
			'Face',
			'ATM',
			'Músculos mastigatórios (masseter e temporal)',
			'Glândulas salivares',
			'Gânglios linfáticos',
			'Lábios e comissuras',
			'Mucosa jugal',
			'Gengiva',
			'Soalho da boca',
			'Língua',
			'Palato',
			'Orofaringe',
			'Percurssão',
			'Exames complementares',
			'Necessidade de periodontia',
			'Necessidade de cirurgia',
			'Necessidade de endodontia',
			'Necessidade de dentística',
			'Necessidade de protese',
			'encaminhamento',
			)
			
class Ficha_DentisticaForm(forms.ModelForm):
    
    class Meta():
        model = Ficha_Dentistica
        fields = (
            'Motivo da consulta:',
            'Quando foi ao dentista pela ultima vez?',
            'Quantas vezes ao dia escova os dentes?',
            'Qual horário de escovação?',
	    	'Usa fio dental?',
	    	'Diário alimentar:',
	    	'Frequência de consumo do açucar:',
	    	'Horário do consumo de açucar:',
	    	'Toma algum medicamento? Qual?',
            'Sente o fluxo salivar diminuindo? Desde quando?',
	    	'Caracteristica da placa:',
	    	'Caracteristica da placa:',
	    	'Diagnostico do risco de cárie:',
	    	'Orientação da dieta, tecnica de higienização',
	    	'Evidenciação de placa',
	    	'Profilaxia',
	    	'Flúor fosfato acidulado 1,23%',	
	    	'FLuoreto de sódio neutro 2%',
	    	'Solução de Fluoreto de sódio 0,5%',
	    	'Digluconato de CLorexidina a 2%(gel)',
	    	'SOlução aquosa de Digluconato de Clorexidina a 0,12%(diária)',
	    	'Selamento de fóssulas e fissuras (código do dente):',
			'Remineralização de lesões de cárie ativas em esmalte (código do dente):',	    	
			'Outra medida (especificar):',
	    	'Restauraçôes provissórias:',
	    	'Tratamento expectante (código do dente):',
			'REstaurações com Amálgama (código do dente):',
			'Returação com resina composta (código do dente):',
			'Radiografias (código do dente)',
			'Observações:',
			'Necessidade de encaminhamento',
			)
