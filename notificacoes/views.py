from django.shortcuts import redirect, get_object_or_404
from .models import Notificacao
from django.contrib.auth.decorators import login_required

@login_required
def marcar_lida(request, pk):
    notificacao = get_object_or_404(Notificacao, pk=pk)
    notificacao.lida = True
    notificacao.save()
    if notificacao.url:
        return redirect(notificacao.url)
    return redirect(request.META.get('HTTP_REFERER', 'core:index'))

@login_required
def limpar_notificacoes(request):
    Notificacao.objects.filter(usuario=request.user, lida=False).update(lida=True)
    Notificacao.objects.filter(usuario__isnull=True, lida=False).update(lida=True)
    return redirect(request.META.get('HTTP_REFERER', 'core:index'))
