from django.urls import path
from . import views

app_name = 'prazos'

urlpatterns= [
    path('probatorio/', views.ProbatorioListView.as_view(), name='probatorio'),
    path('probatorio/criar/', views.ProbatorioCreateView.as_view(), name='probatorio_criar'),
    path('probatorio/editar/<int:pk>/', views.ProbatorioUpdateView.as_view(), name='probatorio_editar'),
    path('probatorio/excluir/<int:pk>/', views.ProbatorioDeleteView.as_view(), name='probatorio_excluir'),
]