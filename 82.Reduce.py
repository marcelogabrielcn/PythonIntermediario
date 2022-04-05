"""
Reduce
"""

from dados80 import produtos, pessoas, lista
from functools import reduce

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

soma_preco = reduce(lambda ac, p: ac + p['preco'], produtos, 0)
print(soma_preco)

soma_idade = reduce(lambda ac, i: ac + i['Idade'], pessoas, 0)
print(f'Média de idades: {soma_idade / len(pessoas)}')
