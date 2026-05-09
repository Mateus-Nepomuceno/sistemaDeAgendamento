from django.contrib import admin
from .models import Probatorio

@admin.register(Probatorio)
class ProbatorioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'data_inicio', 'data_encerramento', 'avaliacao_1', 'avaliacao_2', 'avaliacao_3', 'comentarios', 'suap']
    list_filter = ['nome','matricula','data_encerramento']
    search_fields = ['nome','matricula']