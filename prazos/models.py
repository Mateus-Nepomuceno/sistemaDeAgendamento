from django.db import models
from dateutil.relativedelta import relativedelta

class Probatorio(models.Model):
    class Status(models.TextChoices):
        EM_ANDAMENTO = 'EA','Em andamento'
        FINALIZADO = 'FI', 'Finalizado'
        PENDENTE = 'PE','Pendente'

    nome = models.CharField(max_length=100, verbose_name='Nome')
    matricula = models.CharField(max_length=50,)
    data_inicio = models.DateField(blank=True)
    data_encerramento = models.DateField(blank=True)
    avaliacao_1 = models.CharField(
        max_length=2,
        choices=Status.choices,
        verbose_name='Status',
        default=Status.EM_ANDAMENTO
    )
    avaliacao_2 = models.CharField(
        max_length=2,
        choices=Status.choices,
        verbose_name='Status',
        default=Status.EM_ANDAMENTO
    )
    avaliacao_3 = models.CharField(
        max_length=2,
        choices=Status.choices,
        verbose_name='Status',
        default=Status.EM_ANDAMENTO
    )
    comentarios = models.TextField(null=True, blank=True)
    suap = models.URLField(blank=True, null=True, verbose_name='Suap')
    
    def save(self, *args, **kwargs):
        if self.data_inicio:
            self.data_encerramento = self.data_inicio + relativedelta(years=1)
                
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Probatório'
        verbose_name_plural = 'Probatórios'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome}"