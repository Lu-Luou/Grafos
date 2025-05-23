#! /usr/bin/python

# 1ra Practica Laboratorio
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_stdin(grafo):
    """ DONE
    Recibe como argumento un grafo representado como una lista de tipo:
    Ejemplo Entrada: 
       ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    
    donde el 1er elemento se corresponde a la cantidad de vertices,
    y por ultimo las aristas existentes.

    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    """
    output = ([], [])

    for i in range(1, int(grafo[0]) + 1):
        output[0].append(grafo[i])

    for i in range(int(grafo[0]) + 1, len(grafo)):
        aux = tuple(grafo[i].split())
        output[1].append(aux)

    return output

def lee_grafo_archivo(file_path):
    ''' DONE
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''
    output = ([], [])
    with open(file_path, 'r') as file:
        lines = file.readlines()

        for i in range(1, int(lines[0]) + 1):
            output[0].append(lines[i].strip())

        for i in range(int(lines[0]) + 1, len(lines)):
            aux = tuple(lines[i].strip().split()) # strip elimina espacios y split separa los chars en cadenas
            output[1].append(aux)

    return output

def imprime_grafo_lista(grafo):
    print("Representación del grafo:", grafo)

#################### FIN EJERCICIO PRACTICA ####################
def lee_entrada_1():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada:
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    '''
    data_input = []

    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            data_input.append(line.strip())

    return data_input

def lee_entrada_2():
    count = 0
    try:
        while True:
            line = input()
            count = count + 1
            print('Linea: [{0}]'.format(line))
    except EOFError:
        pass

    print('leidas {0} lineas'.format(count))
