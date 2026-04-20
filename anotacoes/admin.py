from django.contrib import admin
from .models import Anotacao, Funcionario


@admin.register(Anotacao)
class AnotacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'funcionario', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['titulo', 'descricao']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'matricula', 'cargo', 'email', 'status', 'proxima_progressao']
    list_filter = ['tipo','status','cargo','ano_avaliado', 'proxima_progressao']
    search_fields = ['nome','matricula','processo', 'email','cargo']
