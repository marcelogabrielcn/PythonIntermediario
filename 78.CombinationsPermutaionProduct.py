"""
Combinations, Permutation and Product
Combinação - Ordem nao importa
Permutação - Ordem importa
Ambos não repetem os valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

classes = ['Amigo', 'Companheiro', 'Pesquisador', 'Pioneiro', 'Excursionista', 'Guia']

for grupo in combinations(classes, 2):
    print(grupo)

for grupo in permutations(classes, 2):
    print(grupo)

for grupo in product(classes, repeat=2):
    print(grupo)
