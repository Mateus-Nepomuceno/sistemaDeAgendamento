from django.urls import path
from . import views
<<<<<<< HEAD
from .views import TecnicoListView, TecnicoCreateView, TecnicoUpdateView, TecnicoDeleteView
=======
>>>>>>> 6609944defb6047076eb27d27cb72dd0fd6a4466

app_name = 'cadastros'

urlpatterns= [
    path('docentes/', views.DocenteListView.as_view(), name='index'),
    path('docentes/criar/', views.DocenteCreateView.as_view(), name='docente_criar'),
    path('docentes/editar/<int:pk>/', views.DocenteUpdateView.as_view(), name='docente_editar'),
    path('docentes/excluir/<int:pk>/', views.DocenteDeleteView.as_view(), name='docente_excluir'),
<<<<<<< HEAD
    path('tecnicos/', TecnicoListView.as_view(), name='tecnicos'),
    path('tecnicos/novo/', TecnicoCreateView.as_view(), name='tecnico_create'),
    path('tecnicos/<int:pk>/editar/', TecnicoUpdateView.as_view(), name='tecnico_update'),
    path('tecnicos/<int:pk>/delete/', TecnicoDeleteView.as_view(), name='tecnico_delete'),
=======
>>>>>>> 6609944defb6047076eb27d27cb72dd0fd6a4466
]