import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'Grafos')))

from practica1 import *
from practica2 import *
from practica3 import *


def main():
    grafo = lee_entrada_1()
    grafo_lista = lee_grafo_stdin(grafo)
    print("Representación del grafo:", grafo_lista)
    print("Grados de los vértices:", cuenta_grado(grafo_lista))

if __name__ == '__main__':
    main()
