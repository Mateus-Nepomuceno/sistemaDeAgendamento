from django.db import models
from dateutil.relativedelta import relativedelta

class Funcionario(models.Model):    
    class Tipo(models.TextChoices):
        DOCENTE = 'DO','Docente'
        TECNICO = 'TE','Técnico'

    ESCOLHA = [
        (True, 'Sim'), 
        (False, 'Não')
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome')
    cargo = models.CharField(max_length=100, verbose_name='Cargo', blank=True, null=True)
    processo = models.CharField(max_length=100)
    ano_avaliado = models.DateField()
    matricula = models.CharField(max_length=50,)
    proxima_progressao = models.DateField(blank=True)
    ativo = models.BooleanField(verbose_name='Ativo', choices=ESCOLHA, default=True)
    observacoes=models.TextField(null=True, blank=True)
    tipo = models.CharField(
        max_length=2,
        choices=Tipo.choices,
        verbose_name='Tipo'
    )
    email = models.EmailField(blank=True, verbose_name='Email')
    nivel = models.CharField(max_length=2,verbose_name='Nível')
    
    def save(self, *args, **kwargs):
        if self.ano_avaliado and not self.proxima_progressao:
            self.proxima_progressao = self.ano_avaliado + relativedelta(years=1)
                
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome}"