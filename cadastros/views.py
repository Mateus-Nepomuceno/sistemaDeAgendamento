from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from .models import Funcionario

class TecnicoListView(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'cadastros/tecnicos.html' 
    context_object_name = 'tecnicos'

    def get_queryset(self):
        lista = Funcionario.objects.filter(tipo=Funcionario.Tipo.TECNICO)

        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(nome__icontains=busca) |
                Q(matricula__icontains=busca) |
                Q(cargo__icontains=busca) |
                Q(processo__icontains=busca) 
            )

        return lista
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Funcionario.Status.choices
        return context
    
class TecnicoCreateView(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = [
        'nome', 'processo', 'ano_avaliado', 'matricula', 'cargo', 'observacoes', 'nivel', 'email', 'status', 'suap'
    ]
    success_url = reverse_lazy('cadastros:tecnicos')

    def form_valid(self, form):
        form.instance.tipo = Funcionario.Tipo.TECNICO
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class TecnicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    queryset = Funcionario.objects.filter(tipo=Funcionario.Tipo.TECNICO)
    fields = [
        'nome', 'processo', 'ano_avaliado', 'matricula', 'cargo', 'nivel', 'email', 'status', 'observacoes', 'suap'
    ]
    success_url = reverse_lazy('cadastros:tecnicos')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class TecnicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Funcionario
    success_url = reverse_lazy('cadastros:tecnicos')

    def get_queryset(self):
        return Funcionario.objects.filter(tipo=Funcionario.Tipo.TECNICO)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class DocenteListView(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'cadastros/docentes.html'
    context_object_name = 'docentes'

    def get_queryset(self):
        lista = Funcionario.objects.filter(tipo=Funcionario.Tipo.DOCENTE)
                
        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(nome__icontains= busca) |
                Q(matricula__icontains= busca) |
                Q(processo__icontains= busca)
            )

        return lista
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status_choices'] = Funcionario.Status.choices
        return context

class DocenteCreateView(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = [
        'nome', 'processo', 'ano_avaliado', 'matricula', 'observacoes', 'nivel', 'email', 'status', 'suap'
    ]
    success_url = reverse_lazy('cadastros:docentes')

    def form_valid(self, form):
        form.instance.tipo = Funcionario.Tipo.DOCENTE
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class DocenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    queryset = Funcionario.objects.filter(tipo=Funcionario.Tipo.DOCENTE)
    fields = [
        'nome', 'processo', 'ano_avaliado', 'matricula', 'nivel', 'email', 'status', 'observacoes', 'suap'
    ]
    success_url= reverse_lazy('cadastros:docentes')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class DocenteDeleteView(LoginRequiredMixin, DeleteView):
    model = Funcionario
    success_url = reverse_lazy('cadastros:docentes')

    def get_queryset(self):
        return Funcionario.objects.filter(tipo=Funcionario.Tipo.DOCENTE)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])