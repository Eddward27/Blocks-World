import clase

def setWorld(data): #Transforma los strings de data hacia una representación de los estados inicial y objetivo
    inicial = setEstado(data['estadoInicial'])
    final = setEstado(data['estadoObjetivo'])
    world = { 'inicial': inicial, 'final': final }  #Crea un objeto con ambos estados
    return world

def setEstado(arrTorres):   #Recibe un arreglo de torres representados como string, una sobre otra Ej. ["AB", "CD"] -> A sobre B y C sobre D
    estado = { 'operadores': [], 'estados': [], 'estadosAnteriores': []}
    for strTorre in arrTorres:
        torre = list(strTorre)
        for i in range(0,len(torre)):   #Por cada cubo encontrado, genera un objeto para su representación
            nombre = torre[i]
            on = None
            clear = False
            onTable = True
            if i < len(torre)-1:
                on = torre[i+1]
                onTable = False
            if i == 0:
                clear = True    #Un cubo es Ej. {'nombre': 'A', 'on': 'B', 'clear': True, 'onTable': False}
            estado['estados'].append(clase.cubo(nombre, on, clear, onTable))    #Ingresa el cubo en el arreglo de cubos de representación
    estado['estadosAnteriores'].append(estadoString(estado['estados'])) #Para mostrar la solución se toma el estado inicial como un estado anterior, posteriormente cada operador ejecutado en un estado genera el estado modificado como estado anterior para así tener el camino a seguir hasta la solución
    return estado

def mismoEstado(estado1, estado2):  #Si dos estados son el mismo, independiente de su configuración si una torre esta antes que otra, retorna True
    torres1 = 0
    torres2 = 0
    for cantidad in estado1:
        torres1+=1
    for cantidad in estado2:
        torres2+=1
    if torres1 != torres2:  #Si la cantidad de torres en ambos estados es distinta, es imposible que sean el mismo estado
        return False

    for i in range(0, len(estado1)):    #Ya se verifico que ambos estados podrían ser el mismo sabiendo que tienen misma cantidad de torre, ahora se verifica si efectivamente es el mismo estado
        estadoEncontrado = False
        for j in range(0, len(estado2)):
            if(estado1[i].nombre == estado2[j].nombre): #Por cada cubo en el primer estado se revisan los cubos del otro estado
                if(estado1[i].on == estado2[j].on and estado1[i].onTable == estado2[j].onTable and estado1[i].clear == estado2[j].clear):
                    estadoEncontrado = True #Si se encontró el mismo cubo, se marca un flag para saber si se encontró
                    break   #Como ya se encontró el cubo, no es necesario seguir buscando
        if not estadoEncontrado:    #Si la búsqueda de un cubo resultó inconclusa, no son el mismo estado
            return False
    return True

def estadoString(estado):   #Traduce un estado representado a una lista de Strings que muestran de la forma de entrada un estado
    estadoSTR = []
    for cubosRep in estado: #Primero se buscan los cubos que se encuentran al tope de una torre
        if cubosRep.clear:
            estadoSTR.append(cubosRep.nombre)   #Por cada 'tope' de torre se crea un arreglo que hasta ahora solo contendra el cubo tope de una torre

    for i in range(0,len(estadoSTR)):   #Por cada tope de torre se buscan los cubos que estan por abajo es este
        notLast = True
        cuboActual = estadoSTR[i]
        while notLast:  #Mientras no se llegue a un cubo que este sobre la mesa (fin de torre) se sigue buscando el siguiente
            for j in range(0,len(estado)):
                if cuboActual == estado[j].nombre:  #Si se encuentra el cubo siguiente se agregará a la lista
                    if estado[j].on == None:    #Si el cubo se encuentra en el piso se termina la busqueda de esta torre
                        notLast = False
                        break
                    estadoSTR[i] = estadoSTR[i] + estado[j].on  #Se agrega el cubo a la lista
                    cuboActual = estado[j].on   #Se setea el siguiente cubo a buscar
                    break
    return estadoSTR
