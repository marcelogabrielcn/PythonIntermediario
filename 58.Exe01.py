def func1(v1):
    r1 = func2(v1)
    return r1


def func2(v1):
    v1 = v1 + 10
    return v1


valor = 100
result = func1(valor)
print(result)
