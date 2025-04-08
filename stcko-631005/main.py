import json
import pandas as pd

# Leer el JSON (puede ser un archivo grande)
with open('data.json', 'r') as f:
    raw_data = json.load(f)

# Acceder al contenido
records = []
values = raw_data[0]['data']['values']

for year_entry in values:
    year = year_entry['inventory_year']
    for item in year_entry['values_']:
        variable_uid = item['variable_uid']
        value = item['value']['value']  # Asumimos siempre tipo number
        records.append({
            'inventory_year': year,
            'variable_uid': variable_uid,
            'value': value
        })

# Convertir a DataFrame
df = pd.DataFrame(records)

# Exportar si lo deseas
df.to_csv('output.csv', index=False)