from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Funcionario


"""lista_funcionarios"""
class FuncionarioListView(LoginRequiredMixin, ListView):
    model= Funcionario
    template_name= 'cadastro/lista.html'
    context_object_name= 'funcionarios'


    def get_queryset(self):
        lista= Funcionario.objects.all()

        tipo= self.request.GET.get('tipo')

        if tipo:
            lista= lista.filter(tipo=tipo)
                
        busca= self.request.Get.get('q')
        if busca:
            lista=lista.filter(
                Q(nome_icontains= busca) |
                Q(matricula_icontains= busca) |
                Q(cargo_icontains= busca)
            )

        return lista
    


#criar os funcionarios
class FuncionarioCreateView(LoginRequiredMixin, CreateView):
    model= Funcionario
    template_name= 'cadastro/criar.html'
    fields= [
        'nome', 'cargo', 'processo', 'ano_avaliado', 'matricula', 'status', 'proxima_progressao', 'observacoes', 'tipo', 'email', 'telefone', 'data_contratacao'
    ]

    success_url= reverse_lazy('funcionario_lista')



#Editar os funcionarios
class FuncionarioUpdateView(LoginRequiredMixin, CreateView):
    model= Funcionario
    template_name= 'cadastro/editar.html'
    fields= [
        'nome', 'cargo', 'processo', 'ano_avaliado', 'matricula', 'status', 'proxima_progressao', 'observacoes', 'tipo', 'email', 'telefone', 'data_contratacao'
    ]

    success_url= reverse_lazy('funcionario_lista')

#Deletar os funcionarios
class FuncionarioDeleteView(LoginRequiredMixin, CreateView):
    model= Funcionario
    template_name= 'cadastro/excluir.html'
    success_url= reverse_lazy('funcionario_lista')