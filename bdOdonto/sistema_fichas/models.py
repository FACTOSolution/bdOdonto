from django.db import models
from django.utils import timezone

class aluno (models.Model):
	nome = models.CharField(max_length=50)
	matricula = models.PositiveIntegerField(primary_key=True)
	login = models.CharField(max_length=20)
	senha = models.CharField(max_length=20)

	def publish(self):
        self.save()

    def __str__(self):
        return self.matricula

class professor (models.Model):
	nome = models.CharField(max_length=50)
	code = models.PositiveIntegerField(primary_key=True)
	login = models.CharField(max_length=20)
	senha = models.CharField(max_length=20)

	def publish(self):
        self.save()

    def __str__(self):
        return self.code


class turma (models.Model):
	code = models.CharField(max_length=7, primary_key=True)
	nome = models.CharField(max_length=30)
	prof = models.ForeignKey('professor.code')
	#ficha = models.ForeignKey('ficha.code')

	def publish(self):
        self.save()

    def __str__(self):
        return self.code

class paciente(models.Model):
	cpf = models.PositiveIntegerField(primary_key=True)
	nome = models.CharField(max_length=200)
	endereco = models.CharField(max_length=200)
	bairro = models.CharField(max_length=200)
	cidade = models.CharField(max_length=200)
	estado = models.CharField(max_length=200)
	cep = models.PositiveIntegerField()
	tel = models.PositiveIntegerField()
	cel = models.PositiveIntegerField()
	email  = models.EmailField(blank = True,null=True)
	estado_civil = models.CharField(max_length=200)
	data_nasc = models.DateTimeField()
	idade = models.PositiveIntegerField()
	cor = models.CharField(max_length=200)
	SEXOS = (
		('M','M'),
		('F','F'),
		)
	sexo = models.CharField(max_length=1,choices=SEXOS)
	rg = models.PositiveIntegerField()
	naturalidade = models.CharField(max_length=200)
	nacionalidade = models.CharField(max_length=200)
	profissao_atual = models.CharField(max_length=200,blank = True,null=True)
	profissao_anterior = models.CharField(max_length=200,blank = True,null=True)
	endereco_profissional = models.CharField(max_length=200,blank = True, null = True)
	bairro_profissional = models.CharField(max_length=200,blank = True, null = True)
	cep_profissional = models.PositiveIntegerField(blank = True, null = True)
	
	def publish(self):
        self.save()

    def __str__(self):
        return self.cpf
	


class ficha_diagnostico(models.Model):
	#aluno = models.ForeignKey('aluno.cpf').
    #paciente = models.ForeignKey('paciente')
    numero = models.PositiveIntegerField(primary_key=True)
    data = models.DateTimeField(default=timezone.now)

    motivo = models.CharField(max_length=200)
    historia = models.TextField()

    ultima_consulta = models.DateTimeField(blank = True, null = True)
    frequencia_consultas = models.CharField(max_length=200)
    higiene_propria = models.CharField(max_length=200)
    frequencia_escova = models.PositiveIntegerField()
    dentes_sensiveis = models.BooleanField()
    sangramento_gengiva = models.BooleanField()
    morde_objetos = models.BooleanField()
    mobilidade = models.BooleanField()
    protese = models.BooleanField()
    range_dentes = models.BooleanField()
    dificuldade_abrir = models.BooleanField()
    estalido = models.BooleanField()
    boca_seca = models.BooleanField()
    sol_frequente = models.BooleanField()
    tabagismo = models.BooleanField()
    tipo_tabagismo = models.CharField(max_length=200,blank=True,null=True)
    duracao_tabagismo = models.CharField(max_length=200,blank=True,null=True)
    frequencia_tabagismo = models.CharField(max_length=200,blank=True,null=True)
    tempo_abandono_tabagismo = models.CharField(max_length=200,blank=True,null=True)
    alcool = models.BooleanField()
    frequencia_alcool = models.CharField(max_length=200,blank=True,null=True)
    drogas_ilicitas = models.BooleanField()
    def_drogas_ilicitas = models.CharField(max_length=200,blank=True,null=True)
    tratamento_medico = models.BooleanField()
    def_tratamento_medico = models.CharField(max_length=200,blank=True,null=True)
    medicacao = models.BooleanField()
    def_medicacao = models.CharField(max_length=200,blank=True,null=True)
    doenca_grave = models.BooleanField()
    def_doenca_grave = models.CharField(max_length=200,blank=True,null=True)
    cirurgia = models.BooleanField()
    def_cirurgia = models.CharField(max_length=200,blank=True,null=True)
    anticoncepcional = models.BooleanField()
    gravida = models.BooleanField()
    tempo_gravidez = models.CharField(max_length=200,blank=True,null=True)
    alergia = models.BooleanField()
    def_alergia = models.CharField(max_length=200,blank=True,null=True)
    reacao_medicamento = models.BooleanField()
    def_reacao_medicamento = models.CharField(max_length=200,blank=True,null=True)
    anestesia_dentaria = models.BooleanField()
    reacao_anestesia_dentaria = models.CharField(max_length=200,blank=True,null=True)
    anestesia_geral = models.BooleanField()
    reacao_anestesia_geral = models.CharField(max_length=200,blank=True,null=True)

    D_RESPS = (
    	('P','Pneumonia'),
    	('S','Sinusite'),
    	('R','Rinite'),
    	('B','Bronquite'),
    	('A','Asma'),
    	('O','Outro'),
    	)
    disturbios_respiratorios = models.BooleanField()
    disturbios_respiratorios_abaixo = models.CharField(max_length=1,blank=True,null=True,choices=D_RESPS)
    hipertenso = models.BooleanField()
    pressao_arterial = models.CharField(max_length=200,blank=True,null=True)
    sangramento_excesso = models.BooleanField()
    palpitacao = models.BooleanField()
    falta_ar = models.BooleanField()
    pes_inchados = models.BooleanField()
    febre_reumatica = models.BooleanField()
    problema_cardiovascular = models.BooleanField()
    def_problema_cardiovascular = models.CharField(max_length=200,blank=True,null=True)

    D_TRANS = (
    	('He','Hepatite'),
    	('S','Sifilis'),
    	('T','Tuberculose'),
    	('Ha','Hanseniase'),
    	('A','Aids'),
    	('O','Outro'),
    	)
    doencas_transmissiveis = models.BooleanField()
    doencas_transmissiveis_abaixo = models.CharField(max_length=2,blank=True,null=True,choices=D_RESPS)

    virus = models.BooleanField()
    def_virus = models.CharField(max_length=200,blank=True,null=True)
    diabetes = models.BooleanField()
    cicatrizacao_demorada = models.BooleanField()
    perda_peso = models.BooleanField()
    aumento_freq_urina = models.BooleanField()
    desmaios = models.BooleanField()
    convulsoes = models.BooleanField()
    epilepsia = models.BooleanField()
    disturbio_sanguineo = models.BooleanField()
    def_disturbio_sanguineo = models.CharField(max_length=200,blank=True,null=True)
    outro_problema = models.BooleanField()
    def_outro_problema = models.CharField(max_length=200,blank=True,null=True)


    dentes_sensiveis = models.BooleanField()
    dentes_sensiveis = models.BooleanField()

    face = models.TextField()
    atm = models.TextField()
    m_mastigatorios = models.TextField()
    g_salivares = models.TextField()
    g_linfaticos = models.TextField()
    labios = models.TextField()
    mucosa_j = models.TextField()
    soalho_boca = models.TextField()
    lingua = models.TextField()
    palato = models.TextField()
    orofaringe = models.TextField()
    percussao = models.TextField()
    exames_complementares = models.TextField()

    
    def publish(self):
        self.save()

    def __str__(self):
        return self.numero
