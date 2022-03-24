"""
Count - Contadores infinitos
"""

from itertools import count

contagem = count()

print(next(contagem))
print(next(contagem))
print(next(contagem))
print(next(contagem))

# for v in contagem: CUIDADO
# print(v)

contagem2 = count(start=5, step=2)
for v in contagem2:
    print(v)
    if v >= 20:
        break

lista = ['Marcelo', 'Gabriel', 'Thais', 'Juliana']
contador3 = count()
lista = zip(contador3, lista)
print(list(lista))

