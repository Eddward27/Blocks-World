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
    if tipoBusqueda == 'bfs':   #Tipo de busqueda
        cola = cola + nodosEncontrados
    else:#if tipoBusqueda == 'dfs':
        cola = nodosEncontrados + cola
    largoN = len(nodosEncontrados)  #Largo de lista de nuevos nodos encontrados para futuro print
    nodosEncontrados = []
    print('Largo Q: ' + str(largoQ) + ' - Largo Nodos Nuevos: ' + str(largoN) + ' - Largo Nodos Visitados: ' + str(largoV)) #Se imprimen largo de listas en uso
    return cola

def borrarDuplicados(visitados, nuevos):    #Borra los nodos duplicados de 'nuevos' que ya se encuentren en 'visitados'
    indexDup = []
    for i in range(0, len(nuevos)): #Se verifican todos los estados que se encuentren en 'nuevos'
        for dup in visitados:   #Por cada estado en 'nuevos' se revisa la lista de 'visitados'
            if rep.mismoEstado(dup['estados'], nuevos[i]['estados']):   #Si se encuentra un estado repetido, se guarda su índice para borrarlo cuando la búsqueda de repetidos termine
                indexDup.append(i)
                break   #Si se encontró no es necesario seguir con la busqueda en el resto de la lista de 'visitados'
    indexDup.sort(reverse = True)   #Se ordena la lista de índices de forma descendente para borrar por índice sin alterar el orden con pop()
    for index in indexDup:
        nuevos.pop(index)   #Se borran todos los repetidos
    return nuevos
