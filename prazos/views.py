from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseNotAllowed
from .models import Probatorio

class ProbatorioListView(LoginRequiredMixin, ListView):
    model = Probatorio
    template_name = 'prazos/probatorio.html' 
    context_object_name = 'probatorios'

    def get_queryset(self):
        lista = Probatorio.objects.all()

        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(nome__icontains=busca) |
                Q(matricula__icontains=busca)
            )

        return lista
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Probatorio.Status.choices
        return context
    
class ProbatorioCreateView(LoginRequiredMixin, CreateView):
    model = Probatorio
    fields = [
        'nome', 'matricula', 'data_inicio', 'avaliacao_1', 'avaliacao_2', 'avaliacao_3', 'comentarios', 'suap'
    ]
    success_url = reverse_lazy('prazos:probatorio')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class ProbatorioUpdateView(LoginRequiredMixin, UpdateView):
    model = Probatorio
    queryset = Probatorio.objects.all()
    fields = [
        'nome', 'matricula', 'data_inicio', 'avaliacao_1', 'avaliacao_2', 'avaliacao_3', 'comentarios', 'suap'
    ]
    success_url = reverse_lazy('prazos:probatorio')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class ProbatorioDeleteView(LoginRequiredMixin, DeleteView):
    model = Probatorio
    success_url = reverse_lazy('prazos:probatorio')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])