from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseNotAllowed
from .models import Probatorio, Contrato

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
    

class SubstitutoListView(LoginRequiredMixin, ListView):
    model = Contrato
    template_name = 'prazos/professor_substituto.html'
    context_object_name = 'substitutos'

    def get_queryset(self):
        lista = Contrato.objects.filter(tipo=Contrato.Tipo.SUBSTITUTO)

        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(nome__icontains=busca) |
                Q(matricula__icontains=busca) |
                Q(vaga__icontains=busca)
            )
        return lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Contrato.Status.choices
        return context


class SubstitutoCreateView(LoginRequiredMixin, CreateView):
    model = Contrato
    fields = ['matricula','nome','vaga','data_inicio','prazo','status','suap','comentario']
    success_url = reverse_lazy('prazos:professor_substituto')

    def form_valid(self, form):
        form.instance.tipo = Contrato.Tipo.SUBSTITUTO
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class SubstitutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Contrato
    queryset = Contrato.objects.filter(tipo=Contrato.Tipo.SUBSTITUTO)

    fields = ['matricula','nome','vaga','data_inicio', 'prazo', 'status','suap','comentario']
    success_url = reverse_lazy('prazos:professor_substituto')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class SubstitutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Contrato
    success_url = reverse_lazy('prazos:professor_substituto')

    def get_queryset(self):
        return Contrato.objects.filter(tipo=Contrato.Tipo.SUBSTITUTO)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])