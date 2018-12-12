# -*- coding: utf-8 -*-

import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group, Permission

# Create your models here.

class Hunter(models.Model):
	nome = models.CharField("Nome", max_length = 64)
	email = models.CharField("E-mail", max_length = 64)
	linkedin = models.CharField("Likedin", max_length = 64)

class Situacao(models.Model):
	nome = models.CharField("Nome", max_length = 64)
	descricao = models.TextField()

class Curso(models.Model):
	nome = models.CharField("Nome", max_length = 64)
	descricao = models.TextField(blank=True)

class Faculdade(models.Model):
	nome = models.CharField("Nome", max_length = 64)
	curso = models.ManyToManyField(Curso)
	descricao = models.TextField(blank=True)
	local = models.CharField("Local", max_length = 64)

class Area_Atuacao(models.Model):
	nome = models.CharField("Nome", max_length = 64)
	descricao = models.TextField(blank=True)

class Empresa_Parceira(models.Model):
	area = models.ManyToManyField(Area_Atuacao)
	nome = models.CharField("Nome", max_length = 64)
	vagas_abertas = models.BooleanField(default=False)

class Vaga(models.Model):
	nome = models.CharField("Nome", max_length = 64)
	empresa = models.ForeignKey(Empresa_Parceira, on_delete=models.CASCADE)
	descricao = models.TextField("Descrição", blank=True)
	salario_max = models.FloatField("Salário máximo")
	salario_min = models.FloatField("Salário mínimo")

class Universitario(models.Model):
	situacao = models.ForeignKey(Situacao, on_delete=models.CASCADE)
	hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	faculdade = models.ForeignKey(Faculdade, on_delete=models.CASCADE)
	email = models.CharField("Email", max_length = 64)
	linkedin = models.CharField("Likedin", max_length = 64)
	telefone = models.CharField("Telefone", max_length = 64)
	comentario_hunter = models.TextField("Comentário Hunter", blank = True)
	mes_graduacao = models.IntegerField("Mês graduação")
	ano_graduacao = models.IntegerField("Ano graduação")

class Talento(Universitario):
	vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
	nota_final = models.IntegerField()
	comentario_hunter_final = models.TextField("Comentário Hunter Final", blank = True)
	pretensao_salarial = models.FloatField("Pretensão Salarial")
