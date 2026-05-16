from datetime import date, timedelta
from .models import Notificacao
from prazos.models import Probatorio, Contrato
from cadastros.models import Funcionario
from anotacoes.models import Anotacao
from django.urls import reverse

def gerar_notificacoes():
    hoje = date.today()
    dias_milestones = [0, 7, 15, 30]
    datas_milestones = [hoje + timedelta(days=d) for d in dias_milestones]
    
    probatorios = Probatorio.objects.filter(
        data_encerramento__in=datas_milestones
    ).exclude(avaliacao_3='FI') | Probatorio.objects.filter(
        data_encerramento__lt=hoje
    ).exclude(avaliacao_3='FI')

    for p in probatorios:
        atrasado = p.data_encerramento < hoje
        dias_restantes = (p.data_encerramento - hoje).days
        
        prefixo = "ATRASADO: " if atrasado else f"LEMBRETE ({dias_restantes} dias): "
        if dias_restantes == 0: prefixo = "HOJE: "
        
        titulo = f"{prefixo}Prazo Probatório - {p.nome}"
        mensagem = f"O estágio probatório de {p.nome} {'encerrou' if atrasado else 'encerra'} em {p.data_encerramento.strftime('%d/%m/%Y')}."
        url = reverse('prazos:probatorio')
        
        Notificacao.objects.get_or_create(
            titulo=titulo,
            mensagem=mensagem,
            url=url,
            defaults={'lida': False}
        )

    funcionarios = Funcionario.objects.filter(
        proxima_progressao__in=datas_milestones
    ).exclude(status='FI') | Funcionario.objects.filter(
        proxima_progressao__lt=hoje
    ).exclude(status='FI')

    for f in funcionarios:
        atrasado = f.proxima_progressao < hoje
        dias_restantes = (f.proxima_progressao - hoje).days
        
        prefixo = "ATRASADO: " if atrasado else f"LEMBRETE ({dias_restantes} dias): "
        if dias_restantes == 0: prefixo = "HOJE: "

        titulo = f"{prefixo}Progressão - {f.nome}"
        mensagem = f"A próxima progressão de {f.nome} {'foi' if atrasado else 'é'} em {f.proxima_progressao.strftime('%d/%m/%Y')}."
        url = reverse('cadastros:docentes') if f.tipo == 'DO' else reverse('cadastros:tecnicos')
        
        Notificacao.objects.get_or_create(
            titulo=titulo,
            mensagem=mensagem,
            url=url,
            defaults={'lida': False}
        )

    anotacoes = Anotacao.objects.filter(
        prazo__in=datas_milestones
    ) | Anotacao.objects.filter(
        prazo__lt=hoje
    )

    for a in anotacoes:
        atrasado = a.prazo < hoje
        dias_restantes = (a.prazo - hoje).days
        
        prefixo = "ATRASADO: " if atrasado else f"LEMBRETE ({dias_restantes} dias): "
        if dias_restantes == 0: prefixo = "HOJE: "

        titulo = f"{prefixo}Prazo Anotação - {a.titulo}"
        mensagem = f"O prazo para a anotação '{a.titulo}' {'venceu' if atrasado else 'vence'} em {a.prazo.strftime('%d/%m/%Y')}."
        url = reverse('anotacoes:index')
        
        Notificacao.objects.get_or_create(
            titulo=titulo,
            mensagem=mensagem,
            url=url,
            usuario=a.usuario,
            defaults={'lida': False}
        )

    contratos = Contrato.objects.filter(
        data_encerramento__in=datas_milestones
    ).exclude(status='FI') | Contrato.objects.filter(
        data_encerramento__lt=hoje
    ).exclude(status='FI')

    for c in contratos:
        atrasado = c.data_encerramento < hoje
        dias_restantes = (c.data_encerramento - hoje).days
        
        prefixo = "ATRASADO: " if atrasado else f"LEMBRETE ({dias_restantes} dias): "
        if dias_restantes == 0: prefixo = "HOJE: "

        titulo = f"{prefixo}Prazo Contrato - {c.nome}"
        mensagem = f"O contrato ({c.get_tipo_display()}) de {c.nome} {'encerrou' if atrasado else 'encerra'} em {c.data_encerramento.strftime('%d/%m/%Y')}."
        url = reverse('prazos:professor_substituto')
        
        Notificacao.objects.get_or_create(
            titulo=titulo,
            mensagem=mensagem,
            url=url,
            defaults={'lida': False}
        )
