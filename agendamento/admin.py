# admin.py
from django.contrib import admin
from .models import Anotacao, Funcionario


@admin.register(Anotacao)
class AnotacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'funcionario', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['titulo', 'descricao']


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'email', 'ativo']
    list_filter = ['ativo', 'cargo']
    search_fields = ['nome', 'email']
