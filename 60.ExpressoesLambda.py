"""
Expressões lambda (funções anônimas) em python
"""


def mult(v1, v2):
    return v1 * v2


var = mult(4, 4)

a = lambda x, y: x * y
print(a(4, 4))
