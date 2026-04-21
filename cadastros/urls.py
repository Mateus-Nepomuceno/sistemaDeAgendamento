from django.urls import path
from . import views

urlpatterns= [
    path('', views.DocenteListView.as_view(), name='index'),
    path('criar/', views.DocenteCreateView.as_view(), name='docente_criar'),
    path('editar/<int:pk>/', views.DocenteUpdateView.as_view(), name='docente_editar'),
    path('excluir/<int:pk>/', views.DocenteDeleteView.as_view(), name='docente_excluir'),
]