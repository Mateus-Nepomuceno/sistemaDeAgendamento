from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'matricula', 'cargo', 'email', 'status', 'proxima_progressao']
    list_filter = ['tipo','status','cargo','ano_avaliado', 'proxima_progressao']
    search_fields = ['nome','matricula','processo', 'email','cargo']