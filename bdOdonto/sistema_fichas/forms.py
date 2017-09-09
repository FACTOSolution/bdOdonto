#coding: latin-1
from django.contrib.auth.models import User
from django import forms

from .models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
	
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Nome de Usu�rio',
            'password': 'Senha',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            }
			
class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('matricula',)

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
            'historia_clinica' : 'Hist�ria Cl�nica (condi��es de sa�de)',
            'medicamentos' : 'Medicamentos em uso no momento', 
            'motivo' : 'Motivo da consulta', 
            'diagnostico_provavel' : 'Diagn�stico prov�vel ap�s anamnese', 
            'atend' : 'Atendimento', 
            'atend_outro' : 'Outro',
            'procedimento' : 'Procedimento realizado',
            'encaminhamento' : 'Encaminhamento ou reagendamento', 
            'prescricoes' : 'Prescri��es Medicamentosas', 
            'especialidade' : 'Especialidade em que se enquadrou o atendimento de urg�ncia',
            'especialidade_outro' : 'Outro',
            }

class Ficha_PPRForm(forms.ModelForm):

    class Meta:
        model = Ficha_PPR
        fields = '__all__'
        labels = {
            'class_kennedy_sup':'Classificação de Kennedy (superior)', 
            'tratamento_previo_sup':'Tratamento prévio (superior)', 
            'planejamento_protese_sup':'Planejamento da Prótese Removível: Apoios, tipo e localização, retentores, conector maior, sela. (superior)', 
            'observacoes_sup':'Observações (superior)',
            'class_kennedy_inf':'Classificação de Kennedy (inferior)', 
            'tratamento_previo_inf':'Tratamento prévio (inferior)',
            'planejamento_protese_inf':'Planejamento da Prótese Removível: Apoios, tipo e localização, retentores, conector maior, sela. (inferior)', 
            'observacoes_inf':'Observações (inferior)',
            }

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
        fields = '__all__'
        labels = {
            'sangramento_gengiva':'Suas gengivas sangram quando escova os dentes?',
            'tratamento_gengiva':'Já fez tratamento de gengiva alguma vez?',
            'hemorragia_extrac_dentes':'Já teve hemorragia após extração dos dentes',
            'aparelho_ortodontico':'Já utilizou aparelho ortodôntico?',
            'alergia_anestesia':'É alérgico ou tem reações alérgicas a anestesia dentária?',
            'alergia_antibioticos':'É alérgico ou tem reações alérgicas a penicilina ou outros antibióticos',
            'alergia_sulfas':'É alérgico ou tem reações alérgicas a Sulfas',
            'alergia_aspirina':'É alérgico ou tem reações alérgicas a Aspirina',
            'alergia_outros':'É alérgico ou tem reações alérgicas a Outros medicamentos',
            'alergia_nao_medicamentos':'É alérgico a outra substância que não sejam medicamentos?',
            'quais_alergias':'Qual(is)',
            'cuidados_medicos':'Está atualmente sob cuidados médicos?',
            'motivo_cuidados_medicos':'Qual motivo?',
            'medicamentos':'Está tomando algum medicamento no momento?',
            'quais_medicamentos':'Qual(is)',
            'febre_reumatica':'Você tem ou já teve Febre Reumática?',
            'doencas_cardiovasculares':'Você tem ou já teve Doenças cardiovasculares',
            'diabetes':'Você ou parente tem diabetes?',
            'tonturas':'Voce tem tonturas de vez em quando?',
            'anemia':'Já foi alguma vez tratado de anemia?',
            'acamado':'Esteve acamado por longo tempo nos últimos 5 meses?',
            'inchaco_dor_juntas':'Suas juntas doem ou incham com frequência?',
            'ulcera':'Já teve úlcera no estômago ou duodeno?',
            'figado':'Tem algum problema com o fígado ou vesícula?',
            'tuberculose':'Já teve ou viveu com alguém que tivesse tuberculose?',
            'sangramento_excessivo':'Quando você se corta a ferida sangra muito?',
            'operacao':'Sofreu alguma operação nos últimos 5 anos?',
            'qual_operacao':'Qual?',
            'variacao_peso':'Sofreu variação de peso ultimamente?',
            'radioterapia':'Já fez algum tratamento radioterápico?',
            'regiao_radioterapia':'Qual região?',
            'tempo_radioterapia':'Por quanto tempo?',
            'pressao_arterial':'Tem problemas com pressão arterial?',
            'problema_menstruacao':'Tem ou teve algum problema associado à sua menstruação?',
            'gravida':'Está grávida?',
            'fumante':'É fumante ou ex-fumante?',
            'tempo_abandono_tabagismo':'Há quanto tempo?',
            'cigs_dia':'Quantos cig/dia?',
            'doenca_infec':'É portador de alguma doença infecto-contagiosa?',
            'qual_doenca_infec':'Qual(is)',
            'drogas_ilicitas':'É ou já foi usuário de drogas ilícitas?',
            }

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
        fields = '__all__'
        labels = {
            'em_tratamento':'Está em tratamento médico?',
            'quanto_tempo':'Há quanto tempo?',
            'alguma_cirurgia':'J� foi submetido a alguma cirurgia?',
            'diabetes':'Tem Diabetes?',
            'febre_reumatica':'Febre reumática?',
            'alteracoes_sanguineas':'Alterações Sanguíneas?',
            'doencas_cardiovasculares':'Doença cárdio-vascular?',
            'problemas_hemorragicos':'Problemas hemorrágicos?',
            'hipertensao':'Hipertensão',
            'marcapasso':'É portador de marcapasso?',
            'gravida':'Está grávida?',
            'tempo_gravidez':'De quantos meses?',
            'hepatite':'Já teve hepatite?',
            'tempo_hepatite':'Há quanto tempo?',
            'tipo_hepatite':'Tipo:',
            'uso_de_medicamento':'Faz uso de algum medicamento?',
            'uso_continuo_de_medicamento':'Faz uso continuo de algum medicamento?',
            'alergia':'Tem alergia?',
            'outras_informacoes':'Outras informações sobre sua sa�de',
            'historia_dental':'História Dental',
            'caracteristicas_da_dor':'Características da dor:',
            'uso_analgesicos':'Faz Uso de medicamentos Analgésicos',
            'uso_antiinflamatorios':'Faz Uso de medicamentos Antiinflamatórios',
            'uso_antibiotico':'Faz Uso de medicamentos Antibiótico',
            'dente':'Dente',
            'dor_frio':'Dor exarcebada por Frio',
            'dor_calor':'Dor exarcebada por Calor',
            'dor_percussao_vertical':'Dor exarcebada por Percussão vertical',
            'dor_percussao_horizontal':'Dor exarcebada por Percussão horizontal',
            'dor_palpacao_apical':'Dor exarcebada por Palpação Apical',
            'camara_normal':'Câmara pulpar Normal',
            'camara_calcificada':'Câmara pulpar Calcificada',
            'camara_com_perfuracao':'Câmara pulpar Com perfuração',
            'camara_com_reabsorcao_interna':'Câmara pulpar Com reabsorção interna',
            'canal_amplo':'Canal radicular Amplo',
            'canal_atresiado':'Canal radicular Atresiado',
            'canal_ja_manipulado':'Canal radicular Já manipulado',
            'canal_obturacao_deficiente':'Canal radicular Obturação deficiente',
            'canal_rizogenese_incompleta':'Canal radicular Rizogênese incompleta',
            'canal_instrumento_fraturado':'Canal radicular Instrumento fraturado',
            'canal_fratura_radicular':'Canal radicular Fratura radicular',
            'canal_sobre_obturacao':'Canal radicular Sobre-obturação',
            'canal_reabsorcao_apical':'Canal radicular Reabsorção apical',
            'canal_reabsorcao_externa':'Canal radicular Reabsorção externa',
            'canal_reabsorcao_interna':'Canal radicular Reabsorção interna',
            'canal_perfuracao':'Canal radicular Perfuração',
            'pericemento_normal':'Pericemento Normal',
            'pericemento_espessado':'Pericemento Espessado',
            'pericemento_hipercementose':'Pericemento Hipercementose',
            'periapice_osteite_rarefaciente_difusa':'Periápice Osteíte rarefaciente difusa',
            'periapice_osteite_rarefaciente_circunscrita':'Periápice Osteíte rarefaciente circunscrita',
             }

class Ficha_OrtodontiaForm(forms.ModelForm):

    class Meta:
        model = Ficha_Ortodontia
        fields = {
            'queixa':'Queixa principal',
            'cor':'Cor da pele',
            'doencas':'Doenças',
            'alergias':'Alergias',
            'def_alergias':'Quais alergias?',
            'operacao':'Operação',
            'estado_saude':'Estado geral de sa�de',
            'traumatismo':'Traumatismo em dentes',
            'data_traumatismo':'Data do traumatismo',
            'vontade_correcao':'Tem vontade de corrigir?',
            'aparelho':'Já usou aparelho antes?',
            'tempo_aparelho': 'Tempo de uso do aparelho',
            'observacoes_anamnese':'Observa��es da anamnese',
            'psicologico':'Tipo psicológico',
            'simetria_facial':'Simetria',
            'tipo_facial':'Tipo facial',
            'selamento_labial_frontal':'Selamento Facial',
            'relacao_ls':'Relação Ls/ls em repouso',
            'espessura':'Espessura labial',
            'tonicidade_labial':'Tonicidade labial',
            'tonicidade_mentoniano':'Tonicidade mentoniano',
            'zigomatico_frontal':'Presença de zigomático',
            'observacoes_frontal':'Observações',
            'simetria_sorriso':'Simetria do sorriso',
            'qtd_gengiva_incisos':'Quantidade de gengiva e incisivos',
            'corredor_bucal':'Corredor Bucal',
            'observacoes_frontal_sorrindo':'Observações',
            'perfil':'Perfil',
            'dimensao':'Dimensão vertical',
            'nariz':'Nariz',
            'selamento_labial_perfil':'Selamento labial',
            'maxila':'Maxila',
            'zigomatico_perfil':'Presença do zigomático',
            'angulo_nasolabial':'Ângulo nasolabial',
            'mandibula':'Mandíbula',
            'qtd_mento':'Quantidade de mento',
            'posicao_labio_superior':'Posição do lábio superior',
            'posicao_labio_inferior':'Posição do lábio inferior',
            'sulco_mentolabial':'Sulco mentolabial',
            'observacoes_perfil':'Observações',
            'respiracao':'Respiração',
            'degluticao':'Deglutição',
            'fonacao':'Fonação',
            'habitos':'Hábitos',
            'habitos_outros':'Outros habitos',
            'atm':'ATM',
            'observacoes_funcional':'Observações',
            'dentadura':'Dentatura',
            'erupcao_dentaria':'Erupção dentária',
            'arco_superior':'Arco superior',
            'arco_inferior':'Arco inferior',
            'linha_med_sup':'Linha média superior',
            'linha_med_inf':'Linha média inferior',
            'trespasse_horizontal':'Trespasse horizontal',
            'trespasse_vertical':'Trespasse vertical',
            'mordida_cruzada':'Mordida cruzada',
            'spee_sup':'Curva de Spee superior',
            'spee_inf':'Curva de Spee inferior',
            'relacao_caninos_dir':'Relação Caninos (dir)',
            'relacao_caninos_esq':'Relação Caninos (esq)',
            'relacao_molares_dir':'Relação molares (dir)',
            'relacao_molares_esq':'Relação molares (esq)',
            'angle':'Classificação de Angle',
            'andrews':'Classificação de Andrews',
            'diagnostico':'Diagnóstico',
            'observacoes_oclusal':'Observações oclusal',
            'observacoes_odontograma':'Observações odontograma'
            }

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
            'outro_problema':'Tem algum outro problema de sa�de não citado?',
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
