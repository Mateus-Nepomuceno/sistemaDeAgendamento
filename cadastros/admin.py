from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'processo', 'ano_avaliado', 'matricula', 'ativo', 'proxima_progressao', 'observacoes', 'tipo', 'progrediu']
    list_filter = ['cargo','ano_avaliado','proxima_progressao']
    search_fields = ['nome','matricula','processo','cargo']