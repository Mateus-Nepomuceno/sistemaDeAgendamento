from django.urls import path
from . import views

urlpatterns= [
    path('', views.FuncionarioListView.as_view(), name='funcionario_lista'),
    path('criar/', views.FuncionarioCreateView.as_view(), name='funcionario_criar'),
    path('editar/<int:pk>/', views.FuncionarioUpdateView.as_view(), name='funcionario_editar'),
    path('excluir/<int:pk>/', views.FuncionarioDeleteView.as_view(), name='funcionario_excluir'),
]