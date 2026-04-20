from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Anotacao, Funcionario


class AnotacaoListView(LoginRequiredMixin, ListView):
    model = Anotacao
    template_name = 'anotacao/lista.html'
    context_object_name = 'anotacoes'

    def get_queryset(self):
        lista = Anotacao.objects.filter(usuario=self.request.user)
        
        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(titulo__icontains=busca) |
                Q(descricao__icontains=busca) |
                Q(funcionario__nome__icontains=busca)
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
    template_name = 'anotacao/criar.html'
    fields = ['titulo', 'descricao', 'link', 'funcionario']
    success_url = reverse_lazy('anotacao_lista')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['funcionario'].required = False
        form.fields['funcionario'].queryset = Funcionario.objects.filter(status='ativo')
        return form

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class AnotacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Anotacao
    template_name = 'anotacao/editar.html'
    fields = ['titulo', 'descricao', 'link', 'funcionario']
    success_url = reverse_lazy('anotacao_lista')

    def get_queryset(self):
        return Anotacao.objects.filter(usuario=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['funcionario'].required = False
        form.fields['funcionario'].queryset = Funcionario.objects.filter(status='ativo')
        return form


class AnotacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Anotacao
    template_name = 'anotacao/excluir.html'
    success_url = reverse_lazy('anotacao_lista')

    def get_queryset(self):
        return Anotacao.objects.filter(usuario=self.request.user)
