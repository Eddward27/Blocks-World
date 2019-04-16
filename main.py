import json
import rep
import busqueda
import sys

if(len(sys.argv) != 3): #Si no se ingresa correctamente la cantidad de argumentos se explica cuales son
    print('Debe ingresar dos argumentos en comando de línea:')
    print('Tipo de búsqueda: bfs, dfs')
    print('Mostrar Q: si, no')
    quit()

if(sys.argv[1] != 'bfs' and sys.argv[1] != 'dfs'):  #Si el primer argumento (tipo de busqueda) es erróneo
    print('Por favor ingrese argumento N°1 válido: bfs, dfs')
    quit()

if(sys.argv[2] != 'si' and sys.argv[2] != 'no'):    #Si el segundo argumento (mostrar Q) es erróneo
    print('Por favor ingrese argumento N°2 válido: si, no')
    quit()
if(sys.argv[2] == 'si'):
    mostrarQ = True
else:
    mostrarQ =False


with open('data.json') as json_file:    #Se lee data.json que contiene los estados incial y objetivo
    data = json.load(json_file)
    print(data['estadoInicial'])
    print(data['estadoObjetivo'])

world = rep.setWorld(data)  #Se generan las representaciones
inicial = world['inicial']
final = world['final']

solucion = busqueda.buscarSolucion(inicial, final, sys.argv[1], mostrarQ)  #Se busca una solución

print('Pasos para la solucion:')    #Muestra los estados hasta la solucion
for paso in solucion['estadosAnteriores']:
    print(paso)

print('\nOperadores aplicados:')    #Muestra los operadores aplicados hasta la solucion
for operacion in solucion['operadores']:
    print(operacion)
