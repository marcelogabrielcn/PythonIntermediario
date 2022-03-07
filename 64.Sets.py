"""
Sets em Python (conjuntos)
Não aceitam elementos duplicados
"""

s1 = set()
s2 = {1, 2, 3, 'Marcelo'}

s1.add(4)
s1.add(6)
s1.add(8)
s1.discard(4)
s1.update('Python')

# Usando sets para remover itens duplicados
list1 = [1, 2, 5, 4, 4, 4, 4, 6, 6, 6, 6, 6, 7, 8, 8, 8, 8, 7, 7, 7, 'Marcelo', 'Marcelo']
set1 = set(list1)
list2 = list(set1)

print(list1)
print(set1)
print(list2)

# Union |  (Faz a união de dois sets)
se1 = {1, 2, 3}
se2 = {1, 2, 3, 4}
se3 = se1 | se2
print(se3)

#  Intersection & (Todos elementos presentes nos dois sets)
se4 = se1 & se2
print(se4)

#  Difference - (Elementos que estão apenas no set da esquerda)
se5 = se2 - se1
print(se5)

#  Symmetric_difference ^ (Elementos difrentes que estão em ambos sets, mas não nos 2)
se6 = se1 ^ se2
print(se6)
