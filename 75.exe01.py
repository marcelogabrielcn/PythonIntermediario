"""
Somar duas listas
"""

lista1 = [2, 3, 4, 5]
lista2 = [2, 3, 4, 5, 6, 7, 8, 9]

soma = []

for n in zip(lista1, lista2):
    soma.append(sum(n))

print(soma)

soma2 = [x + y for x, y in zip(lista1, lista2)]
print(soma2)
