import rep
import operadores
import copy

def buscarSolucion(inicial, final, tipoBusqueda, verLista): #Busca la solución al problema
    estadoInicial = inicial.copy()
    estadoFinal = final.copy()
    if rep.mismoEstado(estadoInicial['estados'], estadoFinal['estados']):   #Verifica si el estado inicial es el final
        print('Estado Inicial es el estado Objetivo')
        quit()

    if len(estadoInicial['estados']) != len (estadoFinal['estados']):   #Si no tienen la misma cantidad de cubos es imposible llegar a una solución
        print('La cantidad de cubos de los estados es distinta, no es posible llegar a una solución')
        quit()

    cola = []
    visitados = []
    operadores = []
    cola.append(copy.deepcopy(estadoInicial))
    while True: #Loop de busqueda, hasta que se encuentre una solución o hasta que no se pueda llegar a una
        if rep.mismoEstado(cola[0]['estados'], estadoFinal['estados']): #Si el nodo siguiente a operar es el objetivo, se retorna
            return cola[0]
        cola = busqueda(cola, visitados, tipoBusqueda, verLista)    #Generación de hijos en busqueda
        if len(cola) == 0:  #Si no quedan nodos por visitar, no se pudo encontrar una solución
            break
    print('No se logró encontrar solución')
    quit()

def busqueda(cola, visitados, tipoBusqueda, verLista):
    if len(cola) == 0:  #Si entra una cola de busqueda vacía, es imposible llegar a una solución
        print('La busqueda no encontro solución')
        quit()

    largoQ = len(cola)  #Largo de la cola para futuro print
    largoV = len(visitados) #Largo de lista de nodos ya visitados para futuro print
    visitados.append(copy.deepcopy(cola[0]))
    estadoActual = copy.deepcopy(cola[0])
    nodosEncontrados = []

    if verLista:    #Si se pide, muestra el 'Q' actual (QUE ES REALMENTE EL NODO A OPERAR)
        print('------------------------')
        print('Q actual:')
        for estado in cola:
            print(estado['estadosAnteriores'][-1])
        print('------------------------')

    nCubos = len(estadoActual['estados'])
    for i in range(0, nCubos):  #Por cada cubo en el estado se ve que operadores se pueden aplicar
        estadoAux = copy.deepcopy(estadoActual)

        if estadoActual['estados'][i].toTableValid():   #Si se puede mover a la mesa
            operadores.toTable(estadoAux['estados'][i].nombre, estadoAux)
            nodosEncontrados.append(copy.deepcopy(estadoAux))
            estadoAux = copy.deepcopy(estadoActual)
        for j in range(0, nCubos):  #Ahora vienen los operadores que funcionan con otros cubos, entonces hay que volver a recorrer los cubos
            if estadoActual['estados'][i].tableToTowerValid(estadoActual['estados'][j]):    #Si desde la mesa se puede mover hacia algun otro cubo
                operadores.tableToTower(estadoAux['estados'][i].nombre, estadoActual['estados'][j].nombre, estadoAux)
                nodosEncontrados.append(copy.deepcopy(estadoAux))
                estadoAux = copy.deepcopy(estadoActual)
            if estadoActual['estados'][i].towerToTowerValid(estadoActual['estados'][j]):    #Si desde una torre se puede mover a otra
                operadores.towerToTower(estadoAux['estados'][i].nombre, estadoActual['estados'][j].nombre, estadoAux)
                nodosEncontrados.append(copy.deepcopy(estadoAux))
                estadoAux = copy.deepcopy(estadoActual)
    cola.pop(0) #Ya se opero el estado actual, entonces se quita de la cola
    nuevos = copy.deepcopy(nodosEncontrados)
    nodosEncontrados = borrarDuplicados(visitados, nuevos)  #Se eliminan los nodos encontrados que ya hayan sido visitados
    cola = borrarDuplicados(visitados, cola)    #Se eliminan los nodos que puedan haberse repetido desde distintos estados a uno en común
    if tipoBusqueda == 'bfs':   #Tipo de busqueda
        cola = cola + nodosEncontrados
    else:#if tipoBusqueda == 'dfs':
        cola = nodosEncontrados + cola
    largoN = len(nodosEncontrados)  #Largo de lista de nuevos nodos encontrados para futuro print
    nodosEncontrados = []
    print('Largo Q: ' + str(largoQ) + ' - Largo Nodos Nuevos: ' + str(largoN) + ' - Largo Nodos Visitados: ' + str(largoV)) #Se imprimen largo de listas en uso
    return cola

def borrarDuplicados(visitados, nuevos):    #Borra los nodos duplicados de 'nuevos' que ya se encuentren en 'visitados'
    for dup in visitados:   #Por cada nodo ya visitado se busca si se encuentra en la lista de nodos nuevos
        for nuevo in nuevos:
            if rep.mismoEstado(dup['estados'], nuevo['estados']):   #Si los estados son los mismos, se borra
                nuevos.remove(nuevo)
    return nuevos   #Retorna la lista sin duplicados
