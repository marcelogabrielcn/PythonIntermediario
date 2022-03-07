lista = [1, 2, 3, 4, 4, 4, 5, 6, 5, 1, 2]
temp = []

for x in lista:
    if x not in temp:
        temp.append(x)
    else:
        print(f'Ops, o número {x} é o primeiro duplicado')
        break
