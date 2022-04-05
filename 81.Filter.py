"""
Filter
"""

from dados80 import produtos, pessoas, lista


# filter
nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

# list comprehension
nova_lista2 = [x for x in lista if x > 5]
print(list(nova_lista2))


nova_lista3 = filter(lambda p: p['preco'] > 200, produtos)
for produto in nova_lista3:
    print(produto)


def filtrarMaior(pessoa):
    if pessoa['Idade'] >= 18:
        return True
    else:
        return False


nova_lista4 = filter(filtrarMaior, pessoas)
for pessoa in nova_lista4:
    print(pessoa)
