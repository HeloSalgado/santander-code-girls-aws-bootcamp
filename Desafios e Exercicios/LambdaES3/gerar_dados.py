import json
from random import randint, choice, uniform
from datetime import datetime, timedelta

# Função para gerar uma data aleatória dentro de um intervalo
def random_date():
    today = datetime.now()
    days_ago = randint(1, 30)
    random_date = today - timedelta(days=days_ago)
    return random_date.strftime("%Y-%m-%d")

# Clientes fictícios
clientes = ["Ana Silva", "Bruno Souza", "Carla Pereira", "Daniel Costa", "Eduardo Lima"]

# Gerar registros 
registros = []
for i in range(10):
    registro = {
        "id": f"NF-{i+1}",
        "cliente": choice(clientes),
        "valor": round(uniform(100.0, 5000.0), 2),
        "data_emissao": random_date()
    }
    registros.append(registro)

# Salvar os registros em um arquivo JSON
with open("notas_fiscais.json", "w", encoding="utf-8") as f:
    json.dump(registros, f, ensure_ascii=False, indent=4)

print("Arquivo 'notas_fiscais.json' gerado com sucesso!")