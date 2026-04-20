from django.db import models
from django.contrib.auth.models import User


class Anotacao(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    descricao = models.TextField(verbose_name='Descrição')
    link = models.URLField(blank=True, null=True, verbose_name='Link')
    
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Última Atualização')
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anotacoes')
    
    funcionario = models.ForeignKey('Funcionario', on_delete=models.SET_NULL, blank=True, null=True, related_name='anotacoes')

    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo


class Funcionario(models.Model):    
    TIPO_CHOICES = [
        ('docente','Docente'),('tecnico','Tecnico'),
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    processo=models.CharField(max_length=100,blank=True,null=True)
    ano_avaliado=models.DateField(blank=True,null=True)
    matricula=models.CharField(max_length=50,blank=True,null=True)
    proxima_progressao=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=50,choices=[('ativo','Ativo'),('inativo','Inativo'),('em_progressao','Em Progressao')], default='ativo')
    observacoes=models.TextField(blank=True,null=True)
    tipo=models.CharField(max_length=20,choices=TIPO_CHOICES)
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    data_contratacao = models.DateField(blank=True, null=True, verbose_name='Data de Contratação')
    

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
