import rep

def toTable(cuboNombre, estadoCompleto):    #Mueve un cubo desde una torre hacia la mesa
    estado = estadoCompleto['estados'].copy()
    for i in range(0, len(estado)):
        if estado[i].nombre == cuboNombre:  #Busca el cubo pedido a bajar a la mesa
            if estado[i].toTableValid():    #Verifica si se puede bajar
                wasOn = estado[i].on
                estado[i].on = None
                estado[i].onTable = True    #Modifica su estado para que este representado en la mesa
                estadoCompleto['operadores'].append('Cubo: ' + estadoCompleto['estados'][i].nombre + ' - To Table') #Ingresa registro de accion en operadores
                break
            else:   #Si no se puede bajar no se opera
                return False
    for i in range(0, len(estado)):
        if estado[i].nombre == wasOn:   #Busca el cubo sobre el que se encontraba el original
            estado[i].clear = True  #Queda como clear
            estadoCompleto['estadosAnteriores'].append(rep.estadoString(estado))    #Marca estado actual como estado anterior para mostrar solucion
            estadoCompleto['estados'] = estado.copy()   #Actualiza el estado con la operación realizada
            return True

def tableToTower(cuboTableNombre, cuboTowerNombre, estadoCompleto): #Mueve un cubo desde la mesa a un torre
    estado = estadoCompleto['estados'].copy()
    for i in range(0, len(estado)):
        if estado[i].nombre == cuboTableNombre: #Busca el cubo a mover
            for j in range(0, len(estado)): #Busca el cubo sobre cual mover
                if estado[j].nombre == cuboTowerNombre: #Cuando se encuentra, se guarda su indice
                    indexTower = j
                    break   #Ya no es necesario seguir buscando
            if estado[i].tableToTowerValid(estado[indexTower]): #Verifica si es posible mover el cubo de la mesa sobre el otro
                estado[i].on = estado[indexTower].nombre    #El cubo original queda sobre el otro
                estado[i].onTable = False   #Ya no esta sobre la mesa
                estado[indexTower].clear = False    #El cubo sobre el que se puso ya no esta clear
                estadoCompleto['estados'] = estado.copy()   #Actualiza el estado con la operación realizada
                estadoCompleto['estadosAnteriores'].append(rep.estadoString(estado))    #Marca estado actual como estado anterior para mostrar solucion
                estadoCompleto['operadores'].append('Cubo: ' + estadoCompleto['estados'][i].nombre + ' - To Tower cubo: ' + estadoCompleto['estados'][indexTower].nombre)   #Ingresa registro de accion en operadores
                return True
            break
    return False    #Si no se puede subir no se opera

def towerToTower(cuboMoveNombre, cuboTowerNombre, estadoCompleto):  #Mueve un cubo desde una torre a otra
    estado = estadoCompleto['estados'].copy()
    for i in range(0, len(estado)):
        if estado[i].nombre == cuboMoveNombre:  #Busca el cubo a mover
            for j in range(0, len(estado)): #Busca el cubo sobre cual mover
                if estado[j].nombre == cuboTowerNombre: #Cuando se encuentra, se guarda su indice
                    indexTower = j
                    break   #Ya no es necesario seguir buscando
            for j in range(0, len(estado)): #Se busca el cubo donde estaba el cubo original
                if estado[j].nombre == estado[i].on:    #Cuando se encuentra, se guarda su indice
                    indexWasOn = j
                    break   #Ya no es necesario seguir buscando
            if estado[i].towerToTowerValid(estado[indexTower]): #Verifica si es posible mover el cubo de una torre sobre otra
                estado[i].on = estado[indexTower].nombre    #Se cambia el cubo sobre el que estaba el original
                estado[indexTower].clear = False    #El cubo sobre el que se movio ya no esta clear
                estado[indexWasOn].clear = True #El cubo desde donde se movio el original ahora esta clear
                estadoCompleto['estados'] = estado.copy()   #Actualiza el estado con la operación realizada
                estadoCompleto['estadosAnteriores'].append(rep.estadoString(estado))    #Marca estado actual como estado anterior para mostrar solucion
                estadoCompleto['operadores'].append('Cubo: ' + estadoCompleto['estados'][i].nombre + ' - Tower To Tower cubo: ' + estadoCompleto['estados'][indexTower].nombre) #Ingresa registro de accion en operadores
                return True
            break
    return False    #Si no se puede mover no se opera
