"""
Aula 92. Problema dos parâmetros mutáveis em funções
"""


def lista_clientes(clientes_iteraveis, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteraveis)
    return lista


clientes_cadastrados = ['Lucas']
clientes1 = lista_clientes(
    ['Marcelo', 'Gabriel', 'Larissa'], clientes_cadastrados)
clientes2 = lista_clientes(['João', 'Fernando', 'Edson'])

print(clientes_cadastrados)
print(clientes1)
print(clientes2)
print(clientes_cadastrados)
