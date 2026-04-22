from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from .models import Funcionario

class DocenteListView(LoginRequiredMixin, ListView):
    model = Funcionario
    template_name = 'cadastros/index.html'
    context_object_name = 'docentes'

    def get_queryset(self):
        lista = Funcionario.objects.filter(tipo=Funcionario.Tipo.DOCENTE)
                
        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(nome__icontains= busca) |
                Q(matricula__icontains= busca) |
                Q(cargo__icontains= busca)
            )

        return lista

class DocenteCreateView(LoginRequiredMixin, CreateView):
    model = Funcionario
    fields = [
        'nome', 'processo', 'ano_avaliado', 'matricula', 'observacoes', 'nivel', 'email'
    ]
    success_url = reverse_lazy('cadastros:index')

    def form_valid(self, form):
        form.instance.tipo = Funcionario.Tipo.DOCENTE
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class DocenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Funcionario
    queryset = Funcionario.objects.filter(tipo=Funcionario.Tipo.DOCENTE)
    fields = [
        'nome', 'processo', 'ano_avaliado', 'matricula', 'nivel', 'email', 'ativo', 'observacoes'
    ]
    success_url= reverse_lazy('cadastros:index')

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])

class DocenteDeleteView(LoginRequiredMixin, DeleteView):
    model = Funcionario
    queryset = Funcionario.objects.filter(tipo=Funcionario.Tipo.DOCENTE)
    success_url = reverse_lazy('cadastros:index')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object = self.get_object()
        self.object.ativo = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(['POST'])