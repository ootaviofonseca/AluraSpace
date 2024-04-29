from django.db import models
class Fotografia (models.Model): #classe que representa a tabela de fotografias no banco de dados
    nome = models.CharField(max_length=100, null = False, blank = False)
    legenda = models.CharField(max_length=150, null = False, blank = False)
    categoria = models.CharField(max_length=100, null = False, blank = False)   
    descricao = models.TextField(null = False, blank = False)
    foto = models.CharField(max_length=100, null = False, blank = False)

    def __str__(self):
        return f"Fotografia [nome{self.nome}]"

