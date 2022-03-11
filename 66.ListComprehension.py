"""
Compreenção de listas em Python
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [number for number in list1]
print(list2)

list3 = [number * 2 for number in list1]
print(list3)

list4 = [(n1, n2) for n1 in list1 for n2 in range(3)]
print(list4)

list5 = ['Marcelo', 'Gabriel', 'Binho']
list6 = [v.replace('a', '@') for v in list5]
print(list6)

print('hello')
list7 = list(range(51))
list8 = [n for n in list7 if n % 2 == 0]
print(list8)
