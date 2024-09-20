from django.db import models

# Create your models here.
class Nota(models.Model):
    nome_aluno = models.CharField(max_length = 200)#nome do usuario
    disciplina = models.CharField(max_length = 200)#nome da despesa
    nota_atividades = models.IntegerField(default = 0)#valor
    nota_trabalho = models.IntegerField(default = 0)#dia de venc
    nota_prova = models.IntegerField(default = 0)#mes venc
    media = models.IntegerField(blank = True, default = 0)
   
