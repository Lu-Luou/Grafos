from src.practica1 import *
from src.practica2 import *
from src.practica3 import *


def main():
    grafo = lee_entrada_1()
    grafo_lista = lee_grafo_stdin(grafo)
    imprime_grafo_lista(grafo_lista)
    print("Grados de los vértices:", cuenta_grado(grafo_lista))
    print("Vértices aislados:", vertice_aislado(grafo_lista))

if __name__ == '__main__':
    main()
