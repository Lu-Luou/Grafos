def cuenta_grado(grafo_lista):
    ''' DONE
    Muestra por pantalla los grados de los vertices de un grafo. 
    El argumento esta en formato de lista.
    
    Ejemplo Entrada: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    Ejemplo retorno: 
        {'A': 1, 'B': 3, 'C': 2}
    '''
    vertices, aristas = grafo_lista
    grados = {vertice: 0 for vertice in vertices}

    for arista in aristas:
        origen, destino = arista
        grados[origen] += 1
        grados[destino] += 1

    return grados

def vertice_aislado(grafo_lista):
    ''' DONE
    Dado un grafo en representacion de lista, obtiene una lista de los vértices aislado.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B')])
    Ejemplo formato salida: 
        ['D','E']
    '''
    output = []
    vertices = grafo_lista[0]
    grados = cuenta_grado(grafo_lista)

    for vertice in vertices:
        if grados[vertice] == 0:
            output.append(vertice)

    return output

def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo Entrada: 
        (['A','B','C','D','E'],[('A','B'),('B','C'),('C','B'),('D','E')])
    Ejemplo formato salida: 
        [['A, 'B','C'], ['D','E']]
    '''
    pass

def es_conexo(grafo_lista):
    '''
    Dado un grafo en representacion de lista, y utilizando la función "componentes_conexas"
    devuelve True/False si el grafo es o no conexo.
    '''
    return len(componentes_conexas(grafo_lista)) == 1
