"""
FizzBuzz
"""


def fizzbuzz(num):
    if ((num % 3) == 0) and (num % 5) == 0:
        resp = 'FizzBuzz'
    elif (num % 5) == 0:
        resp = 'Buzz'
    elif(num % 3) == 0:
        resp = 'Fizz'
    else:
        resp = num
    return resp


numero = int(input('Digite um número: '))
result = fizzbuzz(numero)
print(result)
