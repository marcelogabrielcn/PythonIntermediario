"""
Agrupando valores
"""
from itertools import groupby

alunos = [
    {'nome': 'Marcelo', 'Idade': 22},
    {'nome': 'Fernando', 'Idade': 35},
    {'nome': 'João', 'Idade': 30},
    {'nome': 'José', 'Idade': 45},
    {'nome': 'Thiago', 'Idade': 35},
    {'nome': 'Bruno', 'Idade': 22},
    {'nome': 'Edson', 'Idade': 45},
    {'nome': 'Jonny', 'Idade': 25},
    {'nome': 'Alexandre', 'Idade': 25},
    {'nome': 'Murillo', 'Idade': 25},
]
# alunos.sort(key=lambda item: item['Idade'])

# for aluno in alunos:
# print(aluno)

ordena = lambda item: item['Idade']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

#for agrupamentos, valores in alunos_agrupados:
#    print(f'Agrupamento: {agrupamentos}')
 #   for aluno in valores:
  #      print(aluno)
   # print()

for agrupamentos, valores in alunos_agrupados:
    print(f'Agrupamento: {agrupamentos}')

    quantidade = len(list(valores))
    print(f'{quantidade} alunos tem {agrupamentos} anos.')
    print()
