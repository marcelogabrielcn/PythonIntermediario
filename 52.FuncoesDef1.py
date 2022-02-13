"""
Funções (def) em Python - Parte 1
"""


def funcao():
    print('Minha primeira função.')


funcao()


def saudacao(msg, nome):
    print(msg, nome)


saudacao('Olá', 'Marcelo')
# saudacao()  # Vai dar erro porque não passei o argumento.


def saudacao2(msg='Olá', nome='Marcelo'):
    print(msg, nome)


saudacao2()
