def somaper(num, per):
    result = num + ((num/100)*per)
    return result


valor = int(input('Digite um valor: '))
percentual = int(input('Digite a porcentagem para acrescentar: '))
res = somaper(valor, percentual)
print(res)
