import pandas as pd
from datetime import datetime

# Dados válidos (atendem ao contrato)
dados_validos = [
    {
        "email": "cliente1@example.com",
        "data": datetime(2024, 5, 21, 10, 30),
        "valor": 250.75,
        "produto": "Produto A",
        "quantidade": 3,
        "categoria": "categoria1"
    },
    {
        "email": "cliente2@example.com",
        "data": datetime(2024, 6, 10, 14, 15),
        "valor": 99.9,
        "produto": "Produto B",
        "quantidade": 1,
        "categoria": "categoria2"
    }
]

# Dados inválidos (não atendem ao contrato)
dados_invalidos = [
    {
        "email": "cliente_invalido",  # Email inválido
        "data": "2024-13-01",         # Data inválida (mês 13)
        "valor": -50,                 # Valor negativo
        "produto": 123,               # Tipo errado (int)
        "quantidade": 0,              # Quantidade zero (não positiva)
        "categoria": "categoriaX"     # Categoria inexistente
    },
    {
        "email": "cliente3@example.com",
        "data": "não é uma data",     # Tipo errado
        "valor": "cem",               # Tipo errado (string)
        "produto": "Produto C",
        "quantidade": -5,             # Quantidade negativa
        "categoria": None             # Categoria ausente
    }
]

# Criar DataFrames
df_validos = pd.DataFrame(dados_validos)
df_invalidos = pd.DataFrame(dados_invalidos)

# Salvar em Excel
validos_path = "./synth_data/vendas_validas.xlsx"
invalidos_path = "./synth_data/vendas_invalidas.xlsx"


df_validos.to_excel(validos_path, index=False)
df_invalidos.to_excel(invalidos_path, index=False)

(validos_path, invalidos_path)