from django.db import models
from django.contrib.auth.models import User

class Notificacao(models.Model):
    titulo = models.CharField(max_length=255)
    mensagem = models.TextField()
    url = models.CharField(max_length=255, blank=True, null=True)
    lida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificacoes', null=True, blank=True)

    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.titulo
