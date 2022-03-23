"""
Geradores, Iteradores e Iteráveis em Python
"""

import sys
from time import sleep


def gera():
    r = []
    for n in range(100):
        yield n
        #sleep(0.1)
    return r


g = gera()

for v in g:
    print(v)

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

print(l1)
print(l2)
print(next(l2))
#print(next(l1))
print(next(l2))
print(next(l2))
