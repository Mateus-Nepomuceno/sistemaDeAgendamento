from django.urls import path
from . import views

app_name = 'prazos'

urlpatterns= [
    path('probatorio/', views.ProbatorioListView.as_view(), name='probatorio'),
    path('probatorio/criar/', views.ProbatorioCreateView.as_view(), name='probatorio_criar'),
    path('probatorio/editar/<int:pk>/', views.ProbatorioUpdateView.as_view(), name='probatorio_editar'),
    path('probatorio/excluir/<int:pk>/', views.ProbatorioDeleteView.as_view(), name='probatorio_excluir'),
    path('professor-substituto/', views.SubstitutoListView.as_view(), name='professor_substituto'),
    path('professor-substituto/criar/', views.SubstitutoCreateView.as_view(), name='professor_substituto_criar'),
    path('professor-substituto/editar/<int:pk>/', views.SubstitutoUpdateView.as_view(), name='professor_substituto_editar'),
    path('professor-substituto/excluir/<int:pk>/', views.SubstitutoDeleteView.as_view(), name='professor_substituto_excluir'),
    path('importar-csv/', views.upload_prazos_csv, name='importar_csv'),
]