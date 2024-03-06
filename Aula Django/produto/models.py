from django.db import models
import os

def get_upload_path(instance, filname):
    nome_objeto = instance.nome
    extensao = os.path.splitext(filname)[1]
    return f'produtos/{nome_objeto}/{extensao}'


class Produto(models.Model):
    nome = models.CharField(max_length=65)
    descrição = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    quantidade = models.IntegerField(default=0)
    imagem = models.ImageField(upload_to=get_upload_path, blank=True)
