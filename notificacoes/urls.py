from django.urls import path
from . import views

app_name = 'notificacoes'

urlpatterns = [
    path('marcar-lida/<int:pk>/', views.marcar_lida, name='marcar_lida'),
    path('limpar/', views.limpar_notificacoes, name='limpar'),
]
