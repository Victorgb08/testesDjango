from django.db import models
from django.core.exceptions import ValidationError

def validar_ano(value):
    if value < 1450 or value > 2100:
        raise ValidationError("Ano inválido para publicação.")

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.PositiveIntegerField(validators=[validar_ano])
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.titulo} ({self.ano_publicacao}) por {self.autor}"
