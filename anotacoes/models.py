from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Anotacao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    link = models.URLField(blank=True, null=True, verbose_name='Link')
    
    data_criacao = models.DateField(auto_now_add=True, verbose_name='Data de Criação')
    prazo = models.DateField(null=True, blank=True, verbose_name='Prazo')
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anotacoes')

    @property
    def esta_atrasado(self):
        if not self.prazo:
            return False
        return self.prazo < timezone.now().date()
    
    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo