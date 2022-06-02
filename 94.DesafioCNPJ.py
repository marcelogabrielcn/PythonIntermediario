"""
Validador de CNPJ
"""

import re


def valida_cnpj(cnpj):
    cnpj_limpo = remover_carcteres(cnpj)
    d1 = verifica_d1(cnpj_limpo)
    d2 = verifica_d2(cnpj_limpo, d1)

    # print(cnpj_limpo)
    # print(cnpj_limpo[12], cnpj_limpo[13])
    # print(d1)
    # print(d2)
    if int(cnpj_limpo[12]) is d1 and int(cnpj_limpo[13]) == d2:
        return True
    else:
        return False


def remover_carcteres(cnpj):
    # return re.sub(r'[^0-9]', '', cnpj)
    return re.sub(r'\D', '', cnpj)  # Remover tudo que for diferente de 0 a 9


def verifica_d1(cnpj):
    l1 = []
    l2 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    l3 = []
    for num in range(0, 12):
        l1.append(int(cnpj[num]))
    for n in range(0, 12):
        l3.append(l1[n] * l2[n])
    soma = sum(l3)
    dig1 = 11 - (soma % 11)
    if dig1 > 9:
        dig1 = 0
    return dig1


def verifica_d2(cnpj, d1):
    l1 = []
    l2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    l3 = []
    for num in range(0, 12):
        l1.append(int(cnpj[num]))
    l1.append(d1)
    for n in range(0, 13):
        l3.append(l1[n] * l2[n])
    soma = sum(l3)
    dig2 = 11 - (soma % 11)
    if dig2 > 9:
        dig2 = 0
    return dig2


# def compara_cnpj(cnpj_original, cnpj_construido):
# if cnpj_original == cnpj_construido:
#   return True
# else:
#   return False


if __name__ == '__main__':
    print('Verificador de CNPJ\n')
    cnpjUser = str(input('Digite o CNPJ: '))
    if valida_cnpj(cnpjUser):
        print('CNPJ Válido')
    else:
        print('CNPJ Inválido')
