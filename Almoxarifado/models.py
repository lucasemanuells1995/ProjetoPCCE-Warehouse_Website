from pyexpat import model
from tkinter import CASCADE
from django.db import models

    #Abaixo crio uma base de dados no sqlite. Crio também um app para a pergunta (qualquer que eu queira fazer)
class Pergunta(models.Model):
    texto = models.CharField(max_length=255)
    def __str__(self):
        return self.texto

    #Abaixo faço o link entre as alternativas e as perguntas. Caso a pergunta seja deletada, as alternativas
    #linkadas também serão excluídas.
class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_perguntas = models.CharField(max_length=255)  #Texto da alternativa.
    def __str__(self):
        return self.texto_perguntas

    #Abaixo faço o link entre as descrição e as armas. Caso a arma seja deletada, as alternativas
    #linkadas também serão excluídas.
class Descricao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    calibre = models.ForeignKey(Alternativa, default=1, on_delete=models.CASCADE)
    texto_desc = models.TextField(max_length=10000) #Descrição de arma ou munição
    def __str__(self):
        return self.texto_desc

    #Abaixo faço o link entre as descrição e as munições. Caso a munição seja deletada, as alternativas
    #linkadas também serão excluídas.
class Descricao2(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    calibre = models.ForeignKey(Alternativa, default=1, on_delete=models.CASCADE)
    texto_mun = models.TextField(max_length=10000) #Descrição de arma ou munição
    def __str__(self):
        return self.texto_mun

