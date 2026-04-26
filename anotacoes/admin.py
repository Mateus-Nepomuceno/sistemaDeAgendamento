from django.contrib import admin
from .models import Anotacao

@admin.register(Anotacao)
class AnotacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'data_criacao']
    list_filter = ['data_criacao']
    search_fields = ['titulo', 'descricao']