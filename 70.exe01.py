carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

# Jeito 1
soma = 0
for produto in carrinho:
    soma += produto[1]
print(soma)

# Jeito 2
total = sum([float(y) for x, y in carrinho])
print(total)
