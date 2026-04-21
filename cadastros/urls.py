from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns= [
    path('docentes/', views.DocenteListView.as_view(), name='index'),
    path('docentes/criar/', views.DocenteCreateView.as_view(), name='docente_criar'),
    path('docentes/editar/<int:pk>/', views.DocenteUpdateView.as_view(), name='docente_editar'),
    path('docentes/excluir/<int:pk>/', views.DocenteDeleteView.as_view(), name='docente_excluir'),
]