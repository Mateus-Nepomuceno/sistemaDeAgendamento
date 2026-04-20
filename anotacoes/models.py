from django.db import models
from django.contrib.auth.models import User


class Anotacao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    link = models.URLField(blank=True, null=True, verbose_name='Link')
    
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anotacoes')
    
    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo