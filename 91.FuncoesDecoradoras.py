"""
Funções Decoradoras e Decoradores em Python
"""


def master(funcao):
    def ant(*args, **kwargs):
        print('Estou decorada.')
        funcao(*args, **kwargs)
    return ant


@master
def fala_oi():
    print('Olá meu amigo.')


fala_oi()
