# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Anotacao, Funcionario


class AnotacaoListView(LoginRequiredMixin, ListView):
    """Lista as anotações do usuário logado."""
    model = Anotacao
    template_name = 'anotacao/lista.html'
    context_object_name = 'anotacoes'

    def get_queryset(self):
        # Filtra apenas anotações do usuário atual
        lista = Anotacao.objects.filter(usuario=self.request.user)
        
        # Busca por título, descrição ou nome do funcionário
        busca = self.request.GET.get('q')
        if busca:
            lista = lista.filter(
                Q(titulo__icontains=busca) |
                Q(descricao__icontains=busca) |
                Q(funcionario__nome__icontains=busca)
            )
        
        # Ordenação (padrão: mais recente primeiro)
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
    """Cria uma nova anotação."""
    model = Anotacao
    template_name = 'anotacao/criar.html'
    fields = ['titulo', 'descricao', 'link', 'funcionario']
    success_url = reverse_lazy('anotacao_lista')

    def get_form(self, form_class=None):
        # Torna campo funcionário opcional e mostra apenas ativos
        form = super().get_form(form_class)
        form.fields['funcionario'].required = False
        form.fields['funcionario'].queryset = Funcionario.objects.filter(status='ativo')#alterei a parte (ativo=true) para (status='ativo')
        return form

    def form_valid(self, form):
        # Define o usuário como o logado
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class AnotacaoUpdateView(LoginRequiredMixin, UpdateView):
    """Edita uma anotação existente."""
    model = Anotacao
    template_name = 'anotacao/editar.html'
    fields = ['titulo', 'descricao', 'link', 'funcionario']
    success_url = reverse_lazy('anotacao_lista')

    def get_queryset(self):
        # Impede editar anotações de outros usuários
        return Anotacao.objects.filter(usuario=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['funcionario'].required = False
        form.fields['funcionario'].queryset = Funcionario.objects.filter(status='ativo') #alterei a parte (ativo=true) para (status='ativo')
        return form


class AnotacaoDeleteView(LoginRequiredMixin, DeleteView):
    """Exclui uma anotação."""
    model = Anotacao
    template_name = 'anotacao/excluir.html'
    success_url = reverse_lazy('anotacao_lista')

    def get_queryset(self):
        # Impede excluir anotações de outros usuários
        return Anotacao.objects.filter(usuario=self.request.user)
