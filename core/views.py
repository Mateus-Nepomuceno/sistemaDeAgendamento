import calendar
from django.views.generic import TemplateView
from cadastros.models import Funcionario
from django.utils import timezone

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        lista = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            hoje = timezone.now().date()
            
            lista['funcionarios'] = Funcionario.objects.filter(
                proxima_progressao__gte=hoje,
                proxima_progressao__month=hoje.month,
                proxima_progressao__year=hoje.year
            ).exclude(status='FI').order_by('proxima_progressao')[:4]
            
            _, num_dias = calendar.monthrange(hoje.year, hoje.month)
            
            dias_com_progressao = Funcionario.objects.filter(
                proxima_progressao__month=hoje.month,
                proxima_progressao__year=hoje.year
            ).exclude(status='FI').values_list('proxima_progressao__day', flat=True)
            
            lista['dias_calendario'] = range(1, num_dias + 1) 
            lista['dias_destaque'] = list(dias_com_progressao)
            
        return lista