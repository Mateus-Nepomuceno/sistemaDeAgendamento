from django.core.management.base import BaseCommand
from notificacoes.utils import gerar_notificacoes

class Command(BaseCommand):
    help = 'Verifica prazos e gera notificações'

    def handle(self, *args, **options):
        self.stdout.write('Verificando prazos...')
        gerar_notificacoes()
        self.stdout.write(self.style.SUCCESS('Notificações geradas com sucesso!'))
