# models.py
from django.db import models
from django.contrib.auth.models import User


class Anotacao(models.Model):
    """Modelo para armazenar anotações dos usuários."""
    
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    link = models.URLField(blank=True, null=True, verbose_name='Link')
    
    # Data automática - preenchida na criação
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    # Data automática - atualizada a cada edição
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')
    
    # Relacionamento com usuário (se usuário for deletado, anotações são excluídas)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anotacoes')
    
    # Relacionamento opcional com funcionário
    funcionario = models.ForeignKey('Funcionario', on_delete=models.SET_NULL, blank=True, null=True, related_name='anotacoes')

    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo


class Funcionario(models.Model):
    """Modelo para cadastrar funcionários."""
    
    nome = models.CharField(max_length=100, verbose_name='Nome')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    data_contratacao = models.DateField(blank=True, null=True, verbose_name='Data de Contratação')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def __str__(self):
        return self.nome
