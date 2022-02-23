"""
Tuplas em Python
"""

tupla = (1, 2, 3, 'a', 'Python')
# tupla[1] = 7  # Vai dar um erro
lista = list(tupla)

print(lista)
lista[1] = 7
print(lista)

for v in tupla:
    print(v)

t1 = 1, 2, 'Marcelo', 3
t2 = 4, 5, 'Gabriel', 6
t3 = t1 + t2

print(t3)

d1, d2, d3, *_ = t3
print(d1, d2)
print(d3)
