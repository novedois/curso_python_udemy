from itertools import groupby, tee


alunos = [ 
    { 'nome': 'Filipe', 'nota': 'A' },
    { 'nome': 'Letícia', 'nota': 'B' },
    { 'nome': 'Fernanda', 'nota': 'C' },
    { 'nome': 'Pedro', 'nota': 'D' },
    { 'nome': 'Maurício', 'nota': 'B' },
    { 'nome': 'Zhou', 'nota': 'D' },
    { 'nome': 'Gasly', 'nota': 'A' },
    { 'nome': 'Sainz', 'nota': 'C' },
    { 'nome': 'Binotto', 'nota': 'B' },
]

# Se não ordenar, endoida tudo
ordena = lambda item: item['nota']

alunos.sort(key=ordena)

for aluno in alunos:
    print(aluno)

alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')
    
    quantidade = len(list(va1))
    print(f'Quantidade de alunos por agrupamento: {quantidade}')

    for aluno in va2:
        print(f'Nome: {aluno["nome"]}')