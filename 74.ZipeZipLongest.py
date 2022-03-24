"""
Zip e Zip Longest em Python
"""
from itertools import zip_longest, count

cidades = ['São Paulo', 'Rio de Janeiro', 'Caldas Novas', 'Salvador', 'Campo Grande']
estados = ['SP', 'RJ', 'GO', 'BA']

cidades_estados = zip(cidades, estados)
for locais in cidades_estados:
    print(locais)

print(cidades_estados)
print(list(cidades_estados))

cidades_estados2 = zip_longest(estados, cidades, fillvalue='Estado')
print(dict(cidades_estados2))

indice = count()
cidades_estados3 = zip(indice, estados, cidades)

for v in cidades_estados3:
    print(v)
