import pandas as pd

# Dados
dados = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Nome': ['Alice', 'Julia', 'Bruna', 'Daniel', 'Filipe', 'Silvio'],
    'Idade': [19, 22, 28, 34, 28, 48],
    'Profissão': [
        'Direito',
        'Engenharia',
        'Enfermagem',
        'Engenheiro Civil',
        'Cientista da Computação',
        'Engenheiro Eletrônico'
    ]
}

# Criar o DataFrame
df = pd.DataFrame(dados)

# Exibir o DataFrame
print(df)
