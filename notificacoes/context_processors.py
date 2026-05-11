from .models import Notificacao
from django.utils import timezone
from .utils import gerar_notificacoes
from django.core.cache import cache

def notificacoes_context(request):
    if request.user.is_authenticated:
        cache_key = 'last_notification_check'
        if not cache.get(cache_key):
            gerar_notificacoes()
            cache.set(cache_key, True, 60 * 60 * 6)
            
        notificacoes = Notificacao.objects.filter(usuario=request.user) | Notificacao.objects.filter(usuario__isnull=True)
        notificacoes = notificacoes.filter(lida=False).order_by('-data_criacao')
        
        return {
            'notificacoes_lista': notificacoes[:10],
            'notificacoes_count': notificacoes.count()
        }
    return {}
