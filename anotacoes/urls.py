from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnotacaoListView.as_view(), name='anotacao_lista'),
    path('criar/', views.AnotacaoCreateView.as_view(), name='anotacao_criar'),
    path('editar/<int:pk>/', views.AnotacaoUpdateView.as_view(), name='anotacao_editar'),
    path('excluir/<int:pk>/', views.AnotacaoDeleteView.as_view(), name='anotacao_excluir'),
]
