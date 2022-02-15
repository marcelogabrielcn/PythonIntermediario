"""
02 - Crie uma função que recebe 3 números como parâmetros e exibe a soma entre eles.
"""


def soma(n1, n2, n3):
    soma = n1 + n2 + n3
    print(soma)


v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
v3 = int(input('Digite mais um número: '))
soma(v1, v2, v3)
