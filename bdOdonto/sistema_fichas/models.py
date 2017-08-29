#coding: latin-1

from django.db import models
from django.utils import timezone

class Aluno (models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.PositiveIntegerField(primary_key=True)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.matricula

class Tipo_Fichas(models.Model):
    code = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)

    def publish(self):
        self.save()

    def __str__(self):
        return self.code

class Turma (models.Model):
    code = models.CharField(max_length=7, primary_key=True)
    nome = models.CharField(max_length=30)
    fichas = models.ManyToManyField(Tipo_Fichas)
    alunos = models.ManyToManyField(Aluno,through='Turma_Aluno')

    def publish(self):
        self.save()

    def __str__(self):
        return self.code

class Turma_Aluno (models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    code = models.CharField(max_length=7, primary_key=True)
    periodo = models.CharField(max_length=6)

    def publish(self):
        self.save()

    def __str__(self):
        return self.code

class Professor (models.Model):
    nome = models.CharField(max_length=50)
    code = models.PositiveIntegerField(primary_key=True)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    turmas = models.ManyToManyField(Turma)

    def publish(self):
        self.save()

    def __str__(self):
        return self.code

class Paciente(models.Model):
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

    turma_Aluno = models.ManyToManyField(Turma_Aluno, through = "atendimento")

    def publish(self):
        self.save()

    def __str__(self):
        return self.cpf

class Atendimento (models.Model):
    data = models.DateTimeField(default=timezone.now)
    code = models.CharField(max_length=7, primary_key=True)
    tipo_ficha = models.ForeignKey(Tipo_Fichas, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    turma_Aluno = models.ForeignKey(Turma_Aluno, on_delete=models.CASCADE)

class Ficha_Diagnostico(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)

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
    	('Pneumonia','Pneumonia'),
    	('Sinusite','Sinusite'),
    	('Rinite','Rinite'),
    	('Bronquite','Bronquite'),
    	('Asma','Asma'),
    	('Outro','Outro'),
    	)
    disturbios_respiratorios = models.BooleanField()
    disturbios_respiratorios_abaixo = models.CharField(max_length=15,blank=True,null=True,choices=D_RESPS)
    disturbios_respiratorios_outro = models.CharField(max_length=15,blank=True,null=True,)
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
    	('Hepatite','Hepatite'),
    	('Sifilis','Sifilis'),
    	('Tuberculose','Tuberculose'),
    	('Hanseniase','Hanseniase'),
    	('Aids','Aids'),
    	('Outro','Outro'),
    	)
    doencas_transmissiveis = models.BooleanField()
    doencas_transmissiveis_abaixo = models.CharField(max_length=15,blank=True,null=True,choices=D_RESPS)
    doencas_transmissiveis_hepatite = models.CharField(max_length=5,blank=True,null=True,)
    doencas_transmissiveis_outro = models.CharField(max_length=15,blank=True,null=True,)

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

class Ficha_Ortodontia(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)

    queixa = models.CharField(max_length=200)

    CORES = (
    	('Branca','Branca'),
    	('Negra','Negra'),
    	('Amarela','Amarela'),
    	('Parda','Parda')
    	)

    cor = models.CharField(max_length=10,choices=CORES)

    OP_D = (
    	('Nao relata','Não relata'),
    	('Habituais','Habituais'),
    	('Outras','Outras')
    	)

    doencas = models.CharField(max_length=10,choices=OP_D)

    alergias = models.BooleanField()
    def_alergias = models.CharField(max_length= 20, blank=True,null=True)
    operacao = models.BooleanField()
    estado_saude = models.CharField(max_length=15,choices= (('Bom','Bom'),('Regular','Regular'),('Deficiente','Deficiente')))
    traumatismo = models.BooleanField()
    data_traumatismo = models.CharField(max_length=10,blank=True,null=True)
    vontade_correcao = models.CharField(max_length=15,choices= (('Sim','Sim'),('Nao','Não'),('Nao sabe','Não sabe')))
    aparelho = models.BooleanField()
    tempo_aparelho = models.CharField(max_length=10,blank=True,null=True)
    observacoes_anamnese = models.TextField()


    NORMAL = ('Normal','Normal')
    psicologico = models.CharField(max_length=15,choices= (NORMAL,('Extrovertido','Extrovertido'),('Introvertido','Introvertido')))
    simetria_facial = models.BooleanField()
    tipo_facial = models.CharField(max_length=16,choices= (('Dolicofacial','Dólicofacial'),('Mesofacial','Mesofacial'),('Braquifacial','Braquifacial')))
    selamento_labial_frontal = models.BooleanField()
    ESCS = (
    	NORMAL,
    	('Diminuido','Diminuído'),
    	('Aumentado','Aumentado')
    	)
    relacao_ls = models.CharField(max_length=15,choices= ESCS)
    espessura = models.CharField(max_length=15,choices= ESCS)
    tonicidade_labial = models.CharField(max_length=15,choices= ESCS)
    tonicidade_mentoniano = models.CharField(max_length=15,choices= ESCS)
    zigomatico = models.CharField(max_length=15,choices= ESCS)
    observacoes_frontal = models.TextField()

    simetria_sorriso = models.BooleanField()
    qtd_gengiva_incisos = models.CharField(max_length=15,choices= ESCS)
    corredor_bucal = models.CharField(max_length=15,choices= ESCS)
    observacoes_frontal_sorrindo = models.TextField()

    PERF = (
    	("Reto","Reto"),
    	('Concavo','Côncavo'),
    	('Convexo','Convexo')
    	)
    perfil = models.CharField(max_length=15,choices= PERF)

    DIMS = (
    	("1/3 faciais proporcionais","1/3 faciais proporcionais"),
    	("1/3 inf. aumentado","1/3 inf. aumentado"),
    	("1/3 inf. diminuido","1/3 inf. diminuido")
    	)
    dimensao = models.CharField(max_length=30,choices= DIMS)
    nariz = models.CharField(max_length=15,choices= (NORMAL,('Pequeno','Pequeno'),('Grande','Grande')))
    selamento_labial_perfil = models.BooleanField()
    maxila = models.CharField(max_length=15,choices= (NORMAL,('Prostruida','Prostruída'),('Retruida','Retruída')))
    angulo_nasolabial = models.CharField(max_length=15,choices= (NORMAL,('Fechado','Fechado'),('Aberto','Aberto')))
    posicao_labio_superior = models.CharField(max_length=15,choices= (NORMAL,('Curto','Curto'),('Longo','Longo')))
    posicao_labio_inferior = models.CharField(max_length=15,choices= (NORMAL,('Eversao','Eversão')))
    mandibula = models.CharField(max_length=15,choices= (NORMAL,('Prostruida','Prostruída'),('Retruida','Retruída')))
    qtd_mento = models.CharField(max_length=15,choices= (NORMAL,('Deficiente','Deficiente'),('Proeminente','Proeminente')))
    sulco_mentolabial = models.CharField(max_length=15,choices= ESCS)
    observacoes_perfil = models.TextField()
    