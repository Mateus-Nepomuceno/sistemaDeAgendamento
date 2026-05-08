from django.db import models
from dateutil.relativedelta import relativedelta

class Funcionario(models.Model):    
    class Tipo(models.TextChoices):
        DOCENTE = 'DO','Docente'
        TECNICO = 'TE','Técnico'

    class Status(models.TextChoices):
        EM_ANDAMENTO = 'EA','Em andamento'
        FINALIZADO = 'FI', 'Finalizado'
        PENDENTE = 'PE','Pendente'

    nome = models.CharField(max_length=100, verbose_name='Nome')
    cargo = models.CharField(max_length=100, verbose_name='Cargo', blank=True, null=True)
    processo = models.CharField(max_length=100)
    ano_avaliado = models.DateField()
    matricula = models.CharField(max_length=50,)
    proxima_progressao = models.DateField(blank=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        verbose_name='Status',
        default=Status.EM_ANDAMENTO
    )
    observacoes=models.TextField(null=True, blank=True)
    tipo = models.CharField(
        max_length=2,
        choices=Tipo.choices,
        verbose_name='Tipo'
    )
    email = models.EmailField(blank=True, verbose_name='Email')
    nivel = models.CharField(max_length=2,verbose_name='Nível')
    suap = models.URLField(blank=True, null=True, verbose_name='Suap')
    
    def save(self, *args, **kwargs):
        if self.ano_avaliado:
            self.proxima_progressao = self.ano_avaliado + relativedelta(years=1)
                
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome}"