"""
Dicionários em Python
"""

d1 = {'chave': 'Valor'}
d2 = dict(chave='valor')

dici1 = {
    'str': 'valor1',
    123: 'Valor2',
    (1, 2, 3): 'Valor3'
}

print('str' in dici1)
print('str' in d1.keys())
print('valor' in dici1.values())

receber = dici1.get(123)
print(receber)

print(len(dici1))

for k in dici1:
    print(k)

for v in dici1.values():
    print(v)

for kv in dici1.items():
    print(kv)

for kv2 in dici1.items():
    print(kv2[1])

clientes = {
    'cliente1': {
        'nome': 'Marcelo',
        'idade': 22
    },
    'cliente2': {
        'nome': 'Gabriel',
        'idade': 19
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for nome, idade in clientes_v.items():
        print(f'\t{nome} = {idade}')


d3 = {1: 'a', 2: 'b', 3: 'c'}
# v2 = d3
v3 = d3.copy()
