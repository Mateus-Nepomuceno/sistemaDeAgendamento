import csv
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from .models import Probatorio, Contrato

def importar_csv_prazos(arquivo_csv, tipo_importacao):
    file_data = arquivo_csv.read()
    
    try:
        decoded_file = file_data.decode('utf-8').splitlines()
    except UnicodeDecodeError:
        decoded_file = file_data.decode('latin-1').splitlines()

    reader = csv.DictReader(decoded_file)
    hoje = date.today()

    if tipo_importacao == 'PROBATORIO':
        for row in reader:
            data_inicio = datetime.strptime(row['data_inicio'], '%d/%m/%Y').date()
            data_encerramento = data_inicio + relativedelta(years=1)
            
            av1 = row.get('avaliacao_1', 'EA').strip().upper()
            av2 = row.get('avaliacao_2', 'EA').strip().upper()
            av3 = row.get('avaliacao_3', 'EA').strip().upper()

            if data_encerramento < hoje and av3 == 'EA':
                av3 = 'PE'

            Probatorio.objects.create(
                nome=row['nome'],
                matricula=row['matricula'],
                data_inicio=data_inicio,
                data_encerramento=data_encerramento,
                avaliacao_1=av1,
                avaliacao_2=av2,
                avaliacao_3=av3,
                comentarios=row.get('comentarios', ''),
                suap=row.get('suap', '')
            )

    elif tipo_importacao in ['SU', 'EG']:
        for row in reader:
            data_inicio = datetime.strptime(row['data_inicio'], '%d/%m/%Y').date()
            data_encerramento = data_inicio + relativedelta(years=1)

            status_csv = row.get('status', '').strip().upper()
            if status_csv not in ['EA', 'FI', 'PE']:
                status_csv = 'PE' if data_encerramento < hoje else 'EA'

            Contrato.objects.create(
                nome=row['nome'],
                matricula=row['matricula'],
                vaga=row['vaga'],
                data_inicio=data_inicio,
                data_encerramento=data_encerramento,
                prazo=datetime.strptime(row['prazo'], '%d/%m/%Y').date() if row.get('prazo') else None,
                suap=row.get('suap', ''),
                comentario=row.get('comentario', ''),
                tipo=tipo_importacao, 
                status=status_csv
            )

