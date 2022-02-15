"""
Funções (def) em Python - *args **kwargs
"""


def func(*args, **kwargs):
    print(args)

    print(kwargs)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


lista = [1, 2, 3, 4, 5]
print(*lista, sep='-')

lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Marcelo', sobrenome='Sousa', idade=22)
