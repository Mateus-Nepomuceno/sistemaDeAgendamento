import calendar
from django.views.generic import TemplateView
from cadastros.models import Funcionario
from prazos.models import Probatorio
from anotacoes.models import Anotacao
from django.utils import timezone
from itertools import chain
from operator import attrgetter

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        lista = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            hoje = timezone.now().date()
            _, ultimo_dia = calendar.monthrange(hoje.year, hoje.month)
            fim_mes = hoje.replace(day=ultimo_dia)
            
            funcionarios = Funcionario.objects.filter(
                proxima_progressao__lte=fim_mes
            ).exclude(status='FI')
            for f in funcionarios:
                f.data_exibicao = f.proxima_progressao
                f.tipo_demanda = "Progressão"

            probatorios = Probatorio.objects.filter(
                data_encerramento__lte=fim_mes
            ).exclude(avaliacao_3='FI')
            for p in probatorios:
                p.data_exibicao = p.data_encerramento
                p.tipo_demanda = "Estágio Probatório"

            anotacoes = Anotacao.objects.filter(
                usuario=self.request.user,
                prazo__lte=fim_mes
            )
            for a in anotacoes:
                a.data_exibicao = a.prazo
                a.tipo_demanda = "Anotação"
                a.nome = a.titulo

            demandas_unificadas = sorted(
                chain(funcionarios, probatorios, anotacoes),
                key=attrgetter('data_exibicao')
            )
            
            lista['demandas'] = demandas_unificadas[:4]
            
            dias_progressao = set(Funcionario.objects.filter(
                proxima_progressao__month=hoje.month,
                proxima_progressao__year=hoje.year
            ).exclude(status='FI').values_list('proxima_progressao__day', flat=True))
            
            dias_probatorio = set(Probatorio.objects.filter(
                data_encerramento__month=hoje.month,
                data_encerramento__year=hoje.year
            ).exclude(avaliacao_3='FI').values_list('data_encerramento__day', flat=True))
            
            dias_anotacao = set(Anotacao.objects.filter(
                usuario=self.request.user,
                prazo__month=hoje.month,
                prazo__year=hoje.year
            ).values_list('prazo__day', flat=True))
            
            lista['dias_calendario'] = range(1, ultimo_dia + 1) 
            lista['dias_destaque'] = dias_progressao | dias_probatorio | dias_anotacao
            
        return lista
