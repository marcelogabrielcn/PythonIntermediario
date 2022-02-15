"""
Variáveis locais e globais
"""

var = 'Qualquer valor'


def func():
    print(var)


def func2():
    var = 'Outro valor'
    print(var)


func()
func2()

print(var)
