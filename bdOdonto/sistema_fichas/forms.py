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

class Dados_DentesForm(forms.ModelForm):

    class Meta:
        model = Dados_Dentes
        fields = '__all__'
        labels = {
            'placa':'I. Placa'
        }

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

class Ficha_Endodontia_TabelaForm(forms.ModelForm):

    class Meta:
        model = Ficha_Endodontia_Tabela
        fields = '__all__'
        labels = {
            'dente1':'Dente',
            'canal1':'Canal',
            'ponto_referencia1':'Ponto Referência',
            'cad1':'CAD',
            'ctp1':'CTP',
            'crt1':'CRT',
            'iai1':'IAI',
            'iaf1':'IAF',
            'im1':'IM',
            'dente2':'Dente',
            'canal2':'Canal',
            'ponto_referencia2':'Ponto Referência',
            'cad2':'CAD',
            'ctp2':'CTP',
            'crt2':'CRT',
            'iai2':'IAI',
            'iaf2':'IAF',
            'im2':'IM',
            'dente3':'Dente',
            'canal3':'Canal',
            'ponto_referencia3':'Ponto Referência',
            'cad3':'CAD',
            'ctp3':'CTP',
            'crt3':'CRT',
            'iai3':'IAI',
            'iaf3':'IAF',
            'im3':'IM',
        }

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
        fields = '__all__'
        labels = {
            'motivo':'Motivo da consulta',
            'historia':'Historia da doenca atual',
            'ultima_consulta':'Ultima consulta',
            'frequencia_consultas':'Com que frequência costuma ir ao dentista',
            'higiene_propria':'Como você cuida da higiene da sua boca?',
            'frequencia_escova':'Quantas vezes ao dia escova seus dentes?',
            'dentes_sensiveis':'Tem dentes sensiveis ao calor ou frio?',
            'sangramento_gengiva':'Sua gengiva sangra na escovação ou quando usa fio dental?',
            'morde_objetos':'Tem hábito de morder objetos?',
            'mobilidade':'Já notou alguma mobilidade em seus dentes?',
            'protese':'Usa prótese? Que tipo?',
            'range_dentes':'Tem hábito de ranger ou apertar os dentes?',
            'dificuldade_abrir':'Tem dificuldade de abrir a boca na extensão que gostaria? ',
            'estalido':'Quando abre ou fecha a boca, sente algum estalido?',
            'boca_seca':'Sente que sua boca é seca?',
            'sol_frequente':'Costuma se expor frequentemente ao sol?',
            'tabagismo':'Teve ou tem o hábito do tabagismo?',
            'tipo_tabagismo':'Tipo de tabagismo:',
            'duracao_tabagismo':'Duração do hábito:',    
            'tempo_abandono_tabagismo':'Há quanto tempo abandonou o hábito?',
            'alcool':'Consome bebidas alcoólicas?',
            'frequencia_alcool':'Com que frequencia consome bebidas alcoólicas?',
            'drogas_ilicitas':'Usa drogas ilícitas?',
            'def_drogas_ilicitas':'Qual drogas ilícitas você usa?',
            'tratamento_medico':'Está em tratamento médico?',
            'def_tratamento_medico':'Qual',
            'medicacao':'Está tomando alguma medicação no momento?',
            'def_medicacao':'Qual medicação?',
            'doenca_grave':'Já sofreu alguma doença grave?',
            'def_doenca_grave':'Qual doença',
            'cirurgia':'Já se submeteu a alguma cirurgia?',
            'def_cirurgia':'Qual cirurgia?',
            'anticoncepcional':'Faz uso de anticoncepcional?',
            'gravida':'Está grávida?',
            'tempo_gravidez':'Qual o tempo de gestação?',
            'alergia':'Tem algum tipo de alergia?',
            'def_alergia':'Qual alergia?',
            'reacao_medicamento':'Já teve reação a algum medicamento?',
            'def_reacao_medicamento':'Qual medicamento?',
            'anestesia_dentaria':'Já se submeteu à anestesia dentária?',
            'reacao_anestesia_dentaria':'Teve alguma reação?',
            'anestesia_geral':'Já se submeteu à anestesia geral?',
            'reacao_anestesia_geral':'Teve alguma reação?',
            'disturbios_respiratorios':'Tem algum distúrbio respiratório?',
            'disturbios_respiratorios_abaixo':'Qual distúrbio respiratório?',
            'disturbios_respiratorios_outro':'Outro',
            'hipertenso':'É hipertenso?',
            'pressao_arterial':'Qual a sua pressão arterial?',
            'sangramento_excesso':'Sangra muito quando se corta ou extrai dentes?',
            'palpitacao':'Sente o coração bater muito rapidamente?',
            'falta_ar':'Sente falta de ar ou cansaço com esforço leve?',
            'pes_inchados':'Costuma ter pés e pernas inchados?',
            'febre_reumatica':'Teve febre reumática?',
            'problema_cardiovascular':'Tem ou teve algum problema cardiovascular?',
            'def_problema_cardiovascular':'Qual?',
            'doencas_transmissiveis':'Tem ou teve alguma dst(s)?',
            'doencas_transmissiveis_abaixo':'Qual?',
            'doencas_transmissiveis_hepatite':'Qual Hepatite',
            'doencas_transmissiveis_outro':'Outro',
            'virus':'Tem conhecimento de ser portador de algum virus?',
            'def_virus':'Qual?',
            'diabetes':'É diabético?',
            'cicatrizacao_demorada':'Quando se fere, a cicatrização demora a ocorrer?',
            'perda_peso':'Tem perdido peso recentemente, sem causa aparente?',
            'aumento_freq_urina':'Percebeu aumento na frequencia com que urina?',
            'desmaios':'Tem desmaios frequentes?',
            'convulsoes':'Tem (teve) convulsões?',
            'epilepsia':'Tem epilepsia?',
            'disturbio_sanguineo':'É portador de algum disturbio sanguineo?',
            'def_disturbio_sanguineo':'Qual?',
            'outro_problema':'Tem algum outro problema de saúde não citado?',
            'def_outro_problema':'Qual?',
            'face':'Face',
            'atm':'ATM',
            'm_mastigatorios':'Músculos mastigatórios (masseter e temporal)',
            'g_salivares':'Glândulas salivares',
            'g_linfaticos':'Gânglios linfáticos',
            'labios':'Lábios e comissuras',
            'mucosa_j':'Mucosa jugal',
            'gengiva':'Gengiva',
            'soalho_boca':'Soalho da boca',
            'lingua':'Língua',
            'palato':'Palato',
            'orofaringe':'Orofaringe',
            'percussao':'Percurssão',
            'exames_complementares':'Exames complementares',
            'necessidade_perio':'Necessidade de periodontia',
            'necessidade_cirurgia':'Necessidade de cirurgia',
            'necessidade_endo':'Necessidade de endodontia',
            'necessidade_dentistica':'Necessidade de dentística',
            'necessidade_protese':'Necessidade de protese',
            'disc':'Encaminhamento',
            'disc_outro':'Disciplina(s)'
            }
            
class Ficha_DentisticaForm(forms.ModelForm):
    
    class Meta():
        model = Ficha_Dentistica
        fields = '__all__'
        labels = {
            'motivo_consulta':'Motivo da consulta:',
            'ultima_consulta':'Quando foi ao dentista pela ultima vez?',
            'escova_dentes':'Quantas vezes ao dia escova os dentes?',
            'horario_escovacao':'Qual horário de escovação?',
            'usa_fio_dental':'Usa fio dental?',
            'diario_alimentar':'Diário alimentar:',
            'frequencia_consumo_acucar':'Frequência de consumo do açucar:',
            'horario_consumo_acucar':'Horário do consumo de açucar:',
            'toma_medicamento':'Toma algum medicamento? Qual?',
            'fluxo_salivar':'Sente o fluxo salivar diminuindo? Desde quando?',
            'caracteristica_da_placa1':'Caracteristica da placa:',
            'caracteristica_da_placa2':'Caracteristica da placa:',
            'diag_risco_carie':'Diagnostico do risco de cárie:',
            'orientacao':'Orientação da dieta, tecnica de higienização',
            'evidenciacao_de_placa':'Evidenciação de placa',
            'profilaxia':'Profilaxia',
            'fosfato':'Flúor fosfato acidulado 1,23%',    
            'sodio':'FLuoreto de sódio neutro 2%',
            'fluoreto':'Solução de Fluoreto de sódio 0,5%',
            'clorexidina':'Digluconato de CLorexidina a 2%(gel)',
            'aquosa_digluconato':'SOlução aquosa de Digluconato de Clorexidina a 0,12%(diária)',
            'selamento_fissuras':'Selamento de fóssulas e fissuras (código do dente):',
            'remineralizacao_de_lesoes_de_carie':'Remineralização de lesões de cárie ativas em esmalte (código do dente):',            
            'outra_medida':'Outra medida (especificar):',
            'restauracoes_provisorias':'Restauraçôes provissórias:',
            'tratamento_expectante':'Tratamento expectante (código do dente):',
            'restauracoes_com_amalgama':'Restaurações com Amálgama (código do dente):',
            'restauracao_com_resina':'Returação com resina composta (código do dente):',
            'radiografias':'Radiografias (código do dente)',
            'observacoes_dentistica':'Observações:',
            'encaminhamento_para':'Necessidade de encaminhamento'
            }
