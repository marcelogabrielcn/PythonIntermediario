"""
Caminhos, módulos e pacotes, ponto de vista.

As vezes, quando criamos um projeto, temos várias pastas e diretórios, e precisamos importar algo
de outro lugar.
"""

try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except ImportError:
    raise

from pacote1.modulo1 import variavel1


variavel2 = 'Var02'
print(variavel2)
print(variavel1)
