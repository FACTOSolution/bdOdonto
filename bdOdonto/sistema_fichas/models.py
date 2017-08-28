from django.db import models
from django.utils import timezone

from ficha_diagnostico import *

class Aluno (models.Model):
	nome = models.CharField(max_length=50)
	matricula = models.PositiveIntegerField(primary_key=True)
	login = models.CharField(max_length=20)
	senha = models.CharField(max_length=20)

	def publish(self):
        self.save()

    def __str__(self):
        return self.matricula

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

class Tipo_Fichas(models.Models):
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