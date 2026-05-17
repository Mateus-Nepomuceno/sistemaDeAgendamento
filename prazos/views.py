from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Probatorio, Contrato
from .utils import importar_csv_prazos

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

class EstagioListView(LoginRequiredMixin, ListView):
    model = Contrato
    template_name = 'prazos/estagio.html'
    context_object_name = 'estagios'

    def get_queryset(self):
        lista = Contrato.objects.filter(tipo=Contrato.Tipo.ESTAGIARIO)

        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(nome__icontains=busca) |
                Q(matricula__icontains=busca)
            )
        return lista

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Contrato.Status.choices
        return context


class EstagioCreateView(LoginRequiredMixin, CreateView):
    model = Contrato
    fields = ['matricula','nome','data_inicio','prazo','status','suap','comentario']
    success_url = reverse_lazy('prazos:estagio')

    def form_valid(self, form):
        form.instance.tipo = Contrato.Tipo.ESTAGIARIO
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class EstagioUpdateView(LoginRequiredMixin, UpdateView):
    model = Contrato
    queryset = Contrato.objects.filter(tipo=Contrato.Tipo.ESTAGIARIO)

    fields = ['matricula','nome','data_inicio', 'prazo', 'status','suap','comentario']
    success_url = reverse_lazy('prazos:estagio')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])


class EstagioDeleteView(LoginRequiredMixin, DeleteView):
    model = Contrato
    success_url = reverse_lazy('prazos:estagio')

    def get_queryset(self):
        return Contrato.objects.filter(tipo=Contrato.Tipo.ESTAGIARIO)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

@login_required
def upload_prazos_csv(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    tipo = request.POST.get('tipo_importacao')

    if tipo == 'PROBATORIO':
        fallback_url = 'prazos:probatorio'
    elif tipo == 'SU':
        fallback_url = 'prazos:professor_substituto'
    elif tipo == 'EG':
        fallback_url = 'prazos:estagio'
    else:
        return HttpResponseBadRequest("Tipo de importação inválido ou não informado.")

    if request.FILES.get('arquivo_csv'):
        arquivo = request.FILES['arquivo_csv']
        try:
            importar_csv_prazos(arquivo, tipo)
            messages.success(request, 'Importação realizada com sucesso!')
        except Exception as e:
            messages.error(request, f'Erro ao processar arquivo: {e}')
    else:
        messages.error(request, 'Nenhum arquivo foi selecionado para importação.')

    return redirect(request.META.get('HTTP_REFERER', fallback_url))