"""
Funções (def) em Python - Parte 2
"""


def divide(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divide(16, 0)
if divide:
    print(divide)
else:
    print('Conta inválida')
