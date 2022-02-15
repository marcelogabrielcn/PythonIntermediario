"""
01 - Crie uma função que exibe uma saudação com os parâmetros: Saudação e Nome. Informado pelo usuário.
"""


def saudacao(sau='Olá', nm=''):
    print(sau, nm, ':D')


nome = str(input('Digite um nome: '))
sauda = str(input('Digite uma saudação: '))
saudacao(nm=nome, sau=sauda)
