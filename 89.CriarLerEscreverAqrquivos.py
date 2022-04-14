"""
Criando, lendo, escrevendo e apagando arquivos em Python
"""

file = open('PrimeiroArquivo.txt', 'w+')
file.write('Arquivo txt criado pela aula 89\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.write('Linha 4\n')

file.seek(0, 0)  # Posição que inicia a leitura, linha 0 e posição 0

print('Lendo arquivo')
print(file.read())

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0, 0)
print(file.readlines())

# Por uma convenção existem um jeito mais comum de se trabalhar com arquivos txt:

with open('SegundoArquivo.txt', 'w+') as file2:
    file2.write('Line1')
    file2.write('Line2')
    file2.write('Line3')

with open('PrimeiroArquivo.txt', 'r') as file3:
    print(file3.read())

with open('PrimeiroArquivo.txt', 'a+') as file:
    file.write('LinhaX\n')
    file.write('LinhaY\n')
    file.write('LinhaZ\n')
    file.seek(0, 0)
    print(file.read())



file.close()
