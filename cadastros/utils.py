import csv
from datetime import datetime, date
from dateutil.relativedelta import relativedelta 
from .models import Funcionario

def importar_csv_servidores(arquivo_csv, tipo_servidor):
    
    file_data = arquivo_csv.read()
    
    try:
        decoded_file = file_data.decode('utf-8').splitlines()
    except UnicodeDecodeError:
        decoded_file = file_data.decode('latin-1').splitlines()

    reader = csv.DictReader(decoded_file)
    
    hoje = date.today()
    
    for row in reader:
        data_aval = datetime.strptime(row['ano_avaliado'], '%d/%m/%Y').date()
        
        proxima_prog = data_aval + relativedelta(years=1)
        
        status_csv = row.get('status', '').strip().upper()
        
        if status_csv in ['EA', 'FI', 'PE']:
            status_final = status_csv
        else:
            if proxima_prog < hoje:
                status_final = 'PE' 
            else:
                status_final = 'EA'
        
        Funcionario.objects.create(
            nome=row['nome'],
            processo=row['processo'],
            ano_avaliado=data_aval,
            matricula=row['matricula'],
            nivel=row['nivel'],
            cargo=row.get('cargo', ''), 
            observacoes=row.get('observacoes', ''),
            tipo=tipo_servidor,
            status=status_final 
        )