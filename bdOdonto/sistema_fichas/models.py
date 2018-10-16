# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget

class Aluno (models.Model):
    matricula = models.CharField(max_length=15, primary_key=True)
    usuario = models.OneToOneField(User, null= True, on_delete=models.CASCADE, unique=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.matricula

class Turma (models.Model):
    codigo = models.CharField(max_length=13, primary_key=True)
    nome = models.CharField(max_length=30)
    alunos = models.ManyToManyField(Aluno, through='Turma_Aluno')

    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

class Turma_Aluno (models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=6)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.turma)

class Professor (models.Model):
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=15, primary_key=True)
    turmas = models.ManyToManyField(Turma)
    usuario = models.OneToOneField(User, null= True, on_delete=models.CASCADE, unique=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nome
#PODE SER APAGADO ESSAS 4 CLASSES.


class TAP(models.Model):
    cod_prof = models.CharField(max_length=15)
    mat_aluno = models.CharField(max_length=11)
    cod_turma = models.CharField(max_length=15)
    turma = models.CharField(max_length=25)
    aluno = models.CharField(max_length=30)
    prof = models.CharField(max_length=30)
    #adicionar periodo

    def publish(self):
        self.save()

    def __str__(self):
        string = "Turma: " + self.turma + ", Aluno: " + self.aluno + ", Professor: " + self.prof
        return string

#RELAÇÃO COM TURMA TEM QUE SER SUBSTITUIDA POR TAP
class Tipo_Ficha(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    tap = models.ManyToManyField(TAP)

    def publish(self):
        self.save()

    def __str__(self):
        return self.nome

class Paciente(models.Model):
    cpf = models.CharField(max_length = 11, primary_key=True)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cep = models.CharField(max_length=9, blank=True)
    tel = models.CharField(max_length=11, blank=True)
    cel = models.CharField(max_length=11, blank=True)
    email  = models.EmailField(null=True, blank=True)
    estado_civil = models.CharField(max_length=200)
    data_nasc = models.DateField()
    idade = models.CharField(max_length=3)
    cor = models.CharField(max_length=200)
    SEXOS = (
        ('M','M'),
        ('F','F'),
        )
    sexo = models.CharField(max_length=1, choices=SEXOS)
    rg = models.CharField(max_length=8)
    naturalidade = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200)
    profissao_atual = models.CharField(max_length=200, blank = True, null=True)
    profissao_anterior = models.CharField(max_length=200, blank = True, null=True)
    endereco_profissional = models.CharField(max_length=200, blank = True, null = True)
    bairro_profissional = models.CharField(max_length=200, blank = True, null = True)
    cep_profissional = models.CharField(blank=True, null=True, max_length=9)
    tap = models.ManyToManyField(TAP, through='Atendimento')
    termo_cons = models.ImageField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.cpf

#mudar atendimento pra relação TAP - prontuario
class Atendimento (models.Model):
    data = models.DateField(auto_now=True)
    periodo = models.CharField(max_length=6)
    tap = models.ForeignKey(TAP, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.paciente)

#diretorio IMAGEMFIELD
class Exame (models.Model):
    imagem = models.ImageField()
    cpf_p = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)

class Planejamento(models.Model):
    cpf_p = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    tap = models.ForeignKey(TAP, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateField(auto_now=True)

    def __str__(self):
        str_retorno = "TAP: " + str(self.tap)
        return str_retorno


class Procedimento (models.Model):
    tap = models.ForeignKey(TAP, on_delete=models.CASCADE)
    cpf_p = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    descricao = models.CharField(blank = True, null = True, max_length = 2000)
    data = models.DateField(auto_now=True)
    ficha_ou_procedimento = models.BooleanField() #Se o procedimento for cadastrado juntamente com uma ficha, é tipo "Cadastro de ficha" - 1. Se for cadastrado sem ficha, é "Cadastro de procedimento" - 0
    exame = models.BooleanField() 


#TODAS AS FICHAS PEGAM CHAVE ESTRANGEIRA DE PROCEDIMENTO.
class Odontograma(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    pontos = models.TextField(blank=True)

    def publish(self):
        self.save()
    
    def __str__(self):
        return "Odontograma"

class Ficha_Diagnostico(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)

    data = models.DateField(auto_now=True) #remover

    motivo = models.CharField(max_length=200)
    historia = models.TextField()

    ultima_consulta = models.DateField(blank = True, null = True)
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
    gengiva = models.TextField()
    soalho_boca = models.TextField()
    lingua = models.TextField()
    palato = models.TextField()
    orofaringe = models.TextField()
    percussao = models.TextField()
    exames_complementares = models.TextField()

    odontograma = models.OneToOneField(Odontograma,on_delete=models.PROTECT,null=True)
    necessidade_perio = models.TextField(null=True)
    necessidade_cirurgia = models.TextField(null=True)
    necessidade_endo = models.TextField(null=True)
    necessidade_dentistica = models.TextField(null=True)
    necessidade_protese = models.TextField(null=True)

    disc = models.CharField(max_length=15, null=True, choices= (('Estágio I','Estágio I'), ('Estágio II','Estágio II'), ('Estágio III','Estágio III'), ('EstágioIV','Estágio IV'), ('Outro','Outro')))
    disc_outro = models.CharField(max_length=20,blank=True,null=True)

    def publish(self):
        self.save()
    
    def __str__(self):
        return "Diagnóstico"

class Ficha_Ortodontia(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)

    queixa = models.CharField(max_length=200)

    CORES = (
        ('Branca','Branca'),
        ('Negra','Negra'),
        ('Amarela','Amarela'),
        ('Parda','Parda')
        )

    cor = models.CharField(max_length=10,choices=CORES)

    OP_D = (
        ('Não relata','Não relata'),
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
    vontade_correcao = models.CharField(max_length=15,choices= (('Sim','Sim'),('Não','Não'),('Não sabe','Não sabe')))
    aparelho = models.BooleanField()
    tempo_aparelho = models.CharField(max_length=10,blank=True,null=True)
    observacoes_anamnese = models.TextField()

    NORMAL = ('Normal','Normal')
    psicologico = models.CharField(max_length=15,choices= (NORMAL,('Extrovertido','Extrovertido'),('Introvertido','Introvertido')))
    simetria_facial = models.BooleanField()
    tipo_facial = models.CharField(max_length=16,choices= (('Dolicofacial','Dolicofacial'),('Mesofacial','Mesofacial'),('Braquifacial','Braquifacial')))
    selamento_labial_frontal = models.BooleanField()
    ESCS = (
        NORMAL,
        ('Diminuído','Diminuído'),
        ('Aumentado','Aumentado')
        )
    relacao_ls = models.CharField(max_length=15,choices= ESCS)
    espessura = models.CharField(max_length=15,choices= ESCS)
    tonicidade_labial = models.CharField(max_length=15,choices= ESCS)
    tonicidade_mentoniano = models.CharField(max_length=15,choices= ESCS)
    zigomatico_frontal = models.CharField(max_length=15,choices= ESCS)
    observacoes_frontal = models.TextField()

    simetria_sorriso = models.BooleanField()
    qtd_gengiva_incisos = models.CharField(max_length=15,choices= ESCS)
    corredor_bucal = models.CharField(max_length=15,choices= ESCS)
    observacoes_frontal_sorrindo = models.TextField()

    PERF = (
        ("Reto","Reto"),
        ('Côncavo','Côncavo'),
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
    maxila = models.CharField(max_length=15,choices= (NORMAL,('Prostruída','Prostruída'),('Retruída','Retruída')))
    zigomatico_perfil = models.CharField(max_length=15,choices= (NORMAL,('Ausente','Ausente'),('Proeminente','Proeminente')))
    angulo_nasolabial = models.CharField(max_length=15,choices= (NORMAL,('Fechado','Fechado'),('Aberto','Aberto')))
    posicao_labio_superior = models.CharField(max_length=15,choices= (NORMAL,('Curto','Curto'),('Longo','Longo')))
    posicao_labio_inferior = models.CharField(max_length=15,choices= (NORMAL,('Eversão','Eversão')))
    mandibula = models.CharField(max_length=15,choices= (NORMAL,('Prostruída','Prostruída'),('Retruída','Retruída')))
    qtd_mento = models.CharField(max_length=15,choices= (NORMAL,('Deficiente','Deficiente'),('Proeminente','Proeminente')))
    sulco_mentolabial = models.CharField(max_length=15,choices= ESCS)
    observacoes_perfil = models.TextField()
    
    respiracao = models.CharField(max_length=15,choices= (('Nasal','Nasal'),('Bucal','Bucal'),('Naso-Bucal','Naso-Bucal')))
    degluticao = models.CharField(max_length=15,choices= (NORMAL,('Atípica','Atípica')))
    fonacao = models.CharField(max_length=15,choices= (NORMAL,('Atipica','Atípica')))
    habitos = models.CharField(max_length=25,choices= (('Não relata','Não relata'),('Sucção','Sucção'),('Interposição labial','Interposição labial'),('Interposição','Interposição'),('Onicofagia','Onicofagia'),('Outros','Outros')))
    habitos_outros = models.CharField(max_length=20)
    atm = models.TextField()
    observacoes_funcional = models.TextField()

    dentadura = models.CharField(max_length=25,choices= (('Decidua','DecÃ­dua'),('Mista(1o Transit.)','Mista(1o Transit.)'),('Mista(2o Transit.)','Mista(2o Transit.)'),('Mista(Intertransit.)','Mista(Intertransit.)'),('Permanente','Permanente'),('Arco Tipo I','Arco Tipo I'),('Arco Tipo II','Arco Tipo II')))
    erupcao_dentaria = models.CharField(max_length=15,choices= (NORMAL,('Precoce','Precoce'),('Tardia','Tardia')))
    arco_superior = models.CharField(max_length=15,choices= (NORMAL,('Amplo','Amplo'),('AtrÃ©sico','AtrÃ©sico')))
    arco_inferior = models.CharField(max_length=15,choices= (NORMAL,('Amplo','Amplo'),('AtrÃ©sico','AtrÃ©sico')))
    linha_med_sup = models.CharField(max_length=20,choices= (NORMAL,('Desvio p/ direita','Desvio p/ direita'),('Desvio p/ esquerda','Desvio p/ esquerda')))
    linha_med_inf = models.CharField(max_length=20,choices= (NORMAL,('Desvio p/ direita','Desvio p/ direita'),('Desvio p/ esquerda','Desvio p/ esquerda')))
    trespasse_horizontal = models.CharField(max_length=15,choices= (NORMAL,('Aumentado','Aumentado'),('Negativo','Negativo')))
    trespasse_vertical = models.CharField(max_length=17,choices= (NORMAL,('Aumentado','Aumentado'),('Topo','Topo'),('Mordida aberta','Mordida aberta'),('Dentoalveolar','Dentoalveolar'),('EsquelÃ©tica','EsquelÃ©tica')))
    mordida_cruzada = models.CharField(max_length=17,choices= (('Ausente','Ausente'),('Anterior','Anterior'),('Unilateral Verdadeira','Unilateral Verdadeira'),('Unilateral Funcional','Unilateral Funcional'),('Bilateral','Bilateral'),('Localizada','Localizada')))
    spee_sup = models.CharField(max_length=15,choices= (NORMAL,('Acentuada','Acentuada')))
    spee_inf = models.CharField(max_length=15,choices= (NORMAL,('Acentuada','Acentuada')))
    CLASSES = (
        ("Classe I","Classe I"),
        ("Classe II","Classe II"),
        ("Classe III","Classe III"),
        )
    relacao_caninos_dir = models.CharField(max_length=15,choices= CLASSES)
    relacao_caninos_esq = models.CharField(max_length=15,choices= CLASSES)
    relacao_molares_dir = models.CharField(max_length=15,choices= CLASSES)
    relacao_molares_esq = models.CharField(max_length=15,choices= CLASSES)
    angle = models.CharField(max_length=15,choices= (("Classe I","Classe I"),("Classe II, 1a","Classe II, 1a"),("Classe II, 2a","Classe II, 2a"),("Classe III","Classe III"),("Subdiv. direita","Subdiv. direita"),("Subdiv. esquerda","Subdiv. esquerda")))
    andrews = models.CharField(max_length=15,choices= (("Classe I","Classe I"),("Classe II","Classe II"),("Classe III","Classe III"),("1/4","1/4"),("1/2","1/2"),("3/4","3/4"),("Total","Total")))
    diagnostico = models.CharField(max_length=20,choices= (('OclusÃ£o normal','OclusÃ£o normal'),('MÃ¡ oclusÃ£o','MÃ¡ oclusÃ£o')))
    observacoes_oclusal = models.TextField()

    odontograma = models.OneToOneField(Odontograma,on_delete=models.PROTECT)
    observacoes_odontograma = models.TextField()

    def publish(self):
        self.save()
    
    def __str__(self):
        return "Ortodontia"

class Ficha_Periodontia(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)

    ESCS = (
        ('Sim','Sim'),
        ('NÃ£o','NÃ£o'),
        ('NÃ£o sei','NÃ£o sei')
        )

    sangramento_gengiva = models.CharField(max_length=10,choices= ESCS)
    tratamento_gengiva = models.CharField(max_length=10,choices= ESCS)
    hemorragia_extrac_dentes = models.CharField(max_length=10,choices= ESCS)
    aparelho_ortodontico = models.BooleanField()
    alergia_anestesia = models.CharField(max_length=10,choices= ESCS)
    alergia_antibioticos = models.CharField(max_length=10,choices= ESCS)
    alergia_sulfas = models.CharField(max_length=10,choices= ESCS)
    alergia_aspirina = models.CharField(max_length=10,choices= ESCS)
    alergia_outros = models.CharField(max_length=20,blank=True,null=True)
    alergia_nao_medicamentos = models.CharField(max_length=10,choices= ESCS)
    quais_alergias = models.CharField(max_length=20,blank=True,null=True)
    cuidados_medicos = models.BooleanField()
    motivo_cuidados_medicos = models.CharField(max_length=20,blank=True,null=True)
    medicamentos = models.BooleanField()
    quais_medicamentos = models.CharField(max_length=20,blank=True,null=True)
    febre_reumatica = models.CharField(max_length=10,choices= ESCS)
    doencas_cardiovasculares = models.CharField(max_length=10,choices= ESCS)
    diabetes = models.CharField(max_length=10,choices= ESCS)
    tonturas = models.CharField(max_length=10,choices= ESCS)
    anemia = models.CharField(max_length=10,choices= ESCS)
    acamado = models.CharField(max_length=10,choices= ESCS)
    inchaco_dor_juntas = models.CharField(max_length=10,choices= ESCS)
    ulcera = models.CharField(max_length=10,choices= ESCS)
    figado = models.CharField(max_length=10,choices= ESCS)
    tuberculose = models.CharField(max_length=10,choices= ESCS)
    sangramento_excessivo = models.CharField(max_length=10,choices= ESCS)
    operacao = models.CharField(max_length=10,choices= ESCS)
    qual_operacao = models.CharField(max_length=20,blank=True,null=True)
    variacao_peso = models.CharField(max_length=15,choices= (('Aumentou','Aumentou'),('Diminuiu','Diminuiu'),('Sem mudanÃ§as','Sem mudanÃ§as')))
    radioterapia = models.CharField(max_length=10,choices= ESCS)
    regiao_radioterapia = models.CharField(max_length=20,blank=True,null=True)
    tempo_radioterapia = models.CharField(max_length=20,blank=True,null=True)
    pressao_arterial = models.CharField(max_length=10,choices= (('Alta','Alta'),('Baixa','Baixa'),('Normal','Normal')))
    problema_menstruacao = models.CharField(max_length=10,choices= ESCS)
    gravida = models.CharField(max_length=10,choices= ESCS)
    fumante = models.BooleanField()
    tempo_abandono_tabagismo = models.CharField(max_length=20,blank=True,null=True)
    cigs_dia = models.PositiveIntegerField(blank=True,null=True)
    doenca_infec = models.CharField(max_length=10,choices= ESCS)
    qual_doenca_infec = models.CharField(max_length=20,blank=True,null=True)
    drogas_ilicitas = models.BooleanField()

    odontograma = models.OneToOneField(Odontograma,on_delete=models.PROTECT)

    def publish(self):
        self.save()
    
    def __str__(self):
        return "Periodontia"

class Dados_Dentes(models.Model):
    ficha_periodontia = models.ForeignKey(Ficha_Periodontia)
    letra = models.CharField(max_length=3)
    dente = models.PositiveIntegerField(null=True)
    rec = models.PositiveIntegerField()
    placa = models.BooleanField()
    ps = models.PositiveIntegerField()
    ig = models.BooleanField()
    pic = models.PositiveIntegerField()

    def publish(self):
        self.save()

class Ficha_Urgencia(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    
    historia_clinica = models.CharField(max_length=60)
    medicamentos = models.CharField(max_length=60)
    motivo = models.CharField(max_length=60)
    diagnostico_provavel = models.CharField(max_length=20)
    atend = models.CharField(max_length=15,choices= (('EstÃ¡gio III','EstÃ¡gio III'),('EstÃ¡gio IV','EstÃ¡gio IV'),('Outro','Outro')))
    atend_outro = models.CharField(max_length=20,blank=True,null=True)
    procedimento_real = models.CharField(max_length=60)
    encaminhamento = models.CharField(max_length=60,blank=True,null=True)
    prescricoes = models.CharField(max_length=60,blank=True,null=True)
    ESCS = (
        ('Endodontia','Endodontia'),
        ('PrÃ³tese','PrÃ³tese'),
        ('Periodontia','Periodontia'),
        ('DentÃ­stica','DentÃ­stica'),
        ('Cirurgia','Cirurgia'),
        ('Outro','Outro')
        )
    especialidade = models.CharField(max_length=15,choices= ESCS)
    especialidade_outro = models.CharField(max_length=20,blank=True,null=True)

    def publish(self):
        self.save()
    
    def __str__(self):
        return "Urgência"

class Ficha_Endodontia(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    ESCS = (('Sim','Sim'),('NÃ£o','NÃ£o'),('NÃ£o sei','NÃ£o sei'))

    #ANAMNESE
    em_tratamento_med = models.CharField(max_length=15,choices= ESCS)
    quanto_tempo = models.CharField(max_length=10,blank=True,null=True)
    alguma_cirurgia = models.CharField(max_length=50,blank=True,null=True)
    diabetes = models.CharField(max_length=15,choices= ESCS)
    febre_reumatica = models.CharField(max_length=15,choices= ESCS)
    alteracoes_sanguineas = models.CharField(max_length=15,choices= ESCS)
    doencas_cardiovasculares= models.CharField(max_length=15,choices= ESCS)
    problemas_hemorragicos = models.CharField(max_length=15,choices= ESCS)
    hipertensao = models.CharField(max_length=15,choices= ESCS)
    marcapasso = models.CharField(max_length=15,choices= ESCS)
    gravida = models.CharField(max_length=15,choices= ESCS)
    tempo_gravidez = models.CharField(max_length=10, blank=True, null=True)
    hepatite = models.CharField(max_length=15,choices= ESCS)
    tempo_hepatite = models.CharField(max_length=10, blank=True, null=True)
    tipo_hepatite = models.CharField(max_length=15,blank = True, null = True)
    uso_de_medicamento = models.CharField(max_length=50, blank=True, null=True)
    uso_continuo_de_medicamento = models.CharField(max_length=50, blank=True, null=True)
    alergia = models.CharField(max_length=15,choices= ESCS)
    outras_informacoes = models.CharField(max_length=100, blank=True, null=True)

    #HISTORIA DENTAL
    historia_dental = models.CharField(max_length=100, blank=True, null=True)
    caracteristicas_da_dor = models.CharField(max_length=60, blank=True, null=True) 
    uso_analgesicos = models.BooleanField()
    uso_antiinflamatorios = models.BooleanField()
    uso_antibiotico = models.BooleanField()
    dente = models.PositiveIntegerField()

    #EXAME CLÃNICO
    dor_frio = models.BooleanField()
    dor_calor = models.BooleanField()
    dor_percussao_vertical= models.BooleanField()
    dor_percusao_horizontal = models.BooleanField()
    dor_palpacao_apical = models.BooleanField()

    #EXAME RADIOGRAFICO
        #CAMARA PULPAR
    camara_normal= models.BooleanField()
    camara_calcificada= models.BooleanField()
    camara_com_perfuracao= models.BooleanField()
    camara_com_reabsorcao_interna= models.BooleanField()
        #CANAL RADICULAR
    canal_amplo = models.BooleanField()
    canal_atresiado = models.BooleanField()
    canal_ja_manipulado = models.BooleanField()
    canal_obturacao_deficiente = models.BooleanField()
    canal_rizogenese_incompleta = models.BooleanField()
    canal_instrumento_fraturado = models.BooleanField()
    canal_fratura_radicular = models.BooleanField()
    canal_sobre_obturacao = models.BooleanField()
    canal_reabsorcao_apical = models.BooleanField()
    canal_reabsorcao_externa = models.BooleanField()
    canal_reabsorcao_interna = models.BooleanField()
    canal_perfuracao = models.BooleanField()
        #PERICEMENTO
    pericemento_normal = models.BooleanField()
    pericemento_espessado = models.BooleanField()
    pericemento_hipercementose = models.BooleanField()
        #PERIÃPICE
    periapice_osteite_rarefaciente_difusa = models.BooleanField()
    periapice_osteite_rarefaciente_circunscrita = models.BooleanField()

    diag_clinico_provavel = models.CharField(max_length=100)

    def publish(self):
        self.save()
    
    def __str__(self):
        return "Endodontia"

class Ficha_Endodontia_Tabela(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    
    dente1 = models.PositiveIntegerField(blank = True, null = True)
    canal1 = models.CharField(max_length = 20, blank = True, null = True)
    ponto_referencia1 = models.CharField(max_length = 5, blank = True, null = True)
    cad1 = models.PositiveIntegerField(blank = True, null = True)
    ctp1 = models.PositiveIntegerField(blank = True, null = True)
    crt1 = models.PositiveIntegerField(blank = True, null = True)
    iai1 = models.PositiveIntegerField(blank = True, null = True)
    iaf1 = models.PositiveIntegerField(blank = True, null = True)
    im1 = models.PositiveIntegerField(blank = True, null = True)
    dente2 = models.PositiveIntegerField(blank = True, null = True)
    canal2 = models.CharField(max_length = 20, blank = True, null = True)
    ponto_referencia2 = models.CharField(max_length = 5, blank = True, null = True)
    cad2 = models.PositiveIntegerField(blank = True, null = True)
    ctp2 = models.PositiveIntegerField(blank = True, null = True)
    crt2 = models.PositiveIntegerField(blank = True, null = True)
    iai2 = models.PositiveIntegerField(blank = True, null = True)
    iaf2 = models.PositiveIntegerField(blank = True, null = True)
    im2 = models.PositiveIntegerField(blank = True, null = True)
    dente3 = models.PositiveIntegerField(blank = True, null = True)
    canal3 = models.CharField(max_length = 20, blank = True, null = True)
    ponto_referencia3 = models.CharField(max_length = 5, blank = True, null = True)
    cad3 = models.PositiveIntegerField(blank = True, null = True)
    ctp3 = models.PositiveIntegerField(blank = True, null = True)
    crt3 = models.PositiveIntegerField(blank = True, null = True)
    iai3 = models.PositiveIntegerField(blank = True, null = True)
    iaf3 = models.PositiveIntegerField(blank = True, null = True)
    im3 = models.PositiveIntegerField(blank = True, null = True)


    def publish(self):
        self.save()
    
    def __str__(self):
        return "Endodontia-Tabela"

class Ficha_PPR(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)

    class_kennedy_sup = models.TextField()
    tratamento_previo_sup = models.TextField()
    planejamento_protese_sup = models.TextField()
    observacoes_sup = models.TextField()

    class_kennedy_inf = models.TextField()
    tratamento_previo_inf = models.TextField()
    planejamento_protese_inf = models.TextField()
    observacoes_inf = models.TextField()

    def publish(self):
        self.save()
    
    def __str__(self):
        return "PPR"

class Ficha_Dentistica(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    
    #ANAMNESE
    motivo_consulta = models.CharField(max_length=20, blank=True, null=True)
    ultima_consulta = models.CharField(max_length=10, blank=True, null=True)
    escova_dentes = models.CharField(max_length=20, choices = (('1x','1x'),('2x','2x'),('3x','3x')))
    horario_escovacao = models.CharField(max_length=20, blank=True, null=True)
    usa_fio_dental = models.CharField(max_length=10, blank=True, null=True)
    diario_alimentar = models.CharField(max_length=30, blank=True, null=True)
    frequencia_consumo_acucar = models.CharField(max_length=20, choices = (('3x ao dia','3x ao dia'),('5x ao dia','5x ao dia'),('>5x ao dia','>5x ao dia')))
    RESPOSTA = (('Junto Ã s refeiÃ§Ãµes','Junto Ã s refeiÃ§Ãµes'),('Intervalos entre refeiÃ§Ãµes','Intervalos entre refeiÃ§Ãµes'),('Junto Ã s refeiÃ§Ãµes e nos intervalos das mesmas','Junto Ã s refeiÃ§Ãµes e nos intervalos das mesmas') )
    horario_consumo_acucar = models.CharField(max_length=100, choices=(RESPOSTA))
    toma_medicamento = models.CharField(max_length=20, blank=True, null=True)
    fluxo_salivar = models.CharField(max_length=10, blank=True, null=True)
    
    #EVIDENCIAÃÃO DE PLACA
    escolha_placa = (("Flocular e pegajosa","Flocular e pegajosa"), ("Calcificada", "Calcificada"))
    caracteristica_da_placa1 = models.CharField(max_length=30, choices = escolha_placa, null=True)
    caracteristica_da_placa2 = models.CharField(max_length=30, choices = escolha_placa, null=True)
    
    #DIAGNOSTICO DE RISCO DE CÃRIE
    diag_risco_carie = models.CharField(max_length=20, choices = (("Alto", "Alto"), ("Médio", "Médio"), ("Baixo","Baixo")))
    
    #PLANO DE TRATAMENTO
        #ORIENTAÃÃO E MEDIDAS PREVENTIVAS
    orientacao = models.BooleanField(default=False)
    evidenciacao_de_placa = models.BooleanField(default=False)
    profilaxia = models.BooleanField(default=False)
        #APLICAÃÃO DE FLUOR
    fosfato = models.BooleanField(default=False)
    sodio = models.BooleanField(default=False)
    fluoreto = models.BooleanField(default=False)
        #APLICAÃÃO DE CLOREXIDINA
    clorexidina = models.BooleanField(default=False)
    aquosa_digluconato = models.BooleanField(default=False)
    selamento_fissuras = models.CharField(max_length=20, blank=True, null=True)
    remineralizacao_de_lesoes_de_carie = models.CharField(max_length=20, blank=True, null=True)
    outra_medida = models.CharField(max_length=20, blank=True, null=True)
        #MEDIDAS RESTAURADORAS
    restauracoes_provisorias = models.CharField(max_length=20, blank=True, null=True)
    tratamento_expectante = models.CharField(max_length=20, blank=True, null=True)
    restauracoes_com_amalgama = models.CharField(max_length=20, blank=True, null=True)
    restauracao_com_resina = models.CharField(max_length=20, blank=True, null=True)
    radiografias = models.CharField(max_length=20, blank=True, null=True)
    observacoes_dentistica = models.CharField(max_length=20, blank=True, null=True)
        #NECESSIDADES DE ENCAMINHAMENTO
    encaminhamento_para = models.CharField(max_length=20, blank=True, null=True)

    def publish(self):
        self.save()
    
    def __str__(self):
        return "Dentistica"