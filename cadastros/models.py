from django.db import models

class Funcionario(models.Model):    
    TIPO_CHOICES = [
        ('docente','Docente'),('tecnico','Tecnico'),
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    processo=models.CharField(max_length=100,blank=True,null=True)
    ano_avaliado=models.DateField(blank=True,null=True)
    matricula=models.CharField(max_length=50,blank=True,null=True)
    proxima_progressao=models.DateField(blank=True,null=True)
    status=models.CharField(max_length=50,choices=[('ativo','Ativo'),('inativo','Inativo'),('em_progressao','Em Progressao')], default='ativo')
    observacoes=models.TextField(blank=True,null=True)
    tipo=models.CharField(max_length=20,choices=TIPO_CHOICES)
    email = models.EmailField(blank=True, null=True, verbose_name='Email')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    data_contratacao = models.DateField(blank=True, null=True, verbose_name='Data de Contratação')
    

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.tipo})"