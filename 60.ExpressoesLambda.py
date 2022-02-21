"""
Expressões lambda (funções anônimas) em python
"""


def mult(v1, v2):
    return v1 * v2


var = mult(4, 4)

a = lambda x, y: x * y
print(a(4, 4))

lista = [
    ['P1', 120],
    ['P2', 170],
    ['P3', 180],
    ['P4', 20],
    ['P5', 60]
]


def func(item):
    return item[1]


lista.sort(key=func)
print(lista)


lista2 = [
    ['P1', 190],
    ['P2', 230],
    ['P3', 520],
    ['P4', 70],
    ['P5', 6230]
]

lista2.sort(key=lambda item: item[1])
print(lista2)
