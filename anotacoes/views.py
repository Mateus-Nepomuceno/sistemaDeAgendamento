from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Anotacao

class AnotacaoListView(LoginRequiredMixin, ListView):
    model = Anotacao
    template_name = 'anotacoes/index.html'
    context_object_name = 'anotacoes'

    def get_queryset(self):
        lista = Anotacao.objects.filter(usuario=self.request.user)
        
        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(titulo__icontains=busca) |
                Q(descricao__icontains=busca)
            )
        
        ordenar = self.request.GET.get('ordenar')
        if ordenar == 'titulo':
            lista = lista.order_by('titulo')
        elif ordenar == 'titulo_desc':
            lista = lista.order_by('-titulo')
        elif ordenar == 'data':
            lista = lista.order_by('data_criacao')
        else:
            lista = lista.order_by('-data_criacao')
        
        return lista

class AnotacaoCreateView(LoginRequiredMixin, CreateView):
    model = Anotacao
    fields = ['titulo', 'descricao', 'link']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return redirect('index')

class AnotacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Anotacao
    fields = ['titulo', 'descricao', 'link']
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Anotacao.objects.filter(usuario=self.request.user)

    def get(self, request, *args, **kwargs):
        return redirect('index')

class AnotacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Anotacao
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Anotacao.objects.filter(usuario=self.request.user)

    def get(self, request, *args, **kwargs):
        return redirect('index')