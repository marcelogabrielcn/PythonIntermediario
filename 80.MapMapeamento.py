from dados80 import produtos, pessoas, lista

nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))

nova_lista2 = [x * 2 for x in lista]
print(nova_lista2)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_precos = map(aumenta_preco, produtos)

for produto in novos_precos:
    print(produto)

nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)


def aumenta_idade(p):
    p['nova_idade'] = round(p['Idade'] * 1.20)
    return p


nomes2 = map(aumenta_idade, pessoas)

for pessoa in nomes2:
    print(pessoa)
    