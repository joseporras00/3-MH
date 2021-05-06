import random
import math
import re

        

def evaluarNodos(registro1, registro2):
    aux=registro1[::2]
    aux2=registro2[::2]


    l=len(aux)
    l2=len(aux2)
    contador=0
    for i in range(l):
        for j in range(l2):
            if aux[i]==aux2[j]:
                contador=contador+1
                break

    if contador==l:
        return 1
    else:
        return 0

def crearGrafo(registro):
    l=int((len(registro)/2)+1)
    nodos=registro[::2]
    valores=registro[1::2]

    grafo=[]

    fila=[0]
    for i in range(len(nodos)):
        fila.append(nodos[i])
    grafo.append(fila)

    for i in range(len(nodos)):
        fila2=[]
        fila2.append(nodos[i])
        for j in range(len(nodos)):
            if(i != j):
                fila2.append(int(valores[j])-int(valores[i]))
            else:
                fila2.append(0)
        grafo.append(fila2)

    return grafo

#def mejorarGrafo(grafo,registro):

    

def evaluarRestricciones(grafoRest, registro):
    l=list(range(len(grafoRest)))
    aux=l[1::2]
    l2=list(range(len(grafo)))
    aux2=l2[1::2]
    
    ret=1
    while ret!=0:
        for i in aux2:
            print(grafo[i+1])
            for j in aux:
                print(grafoRest[j+1][1])
                if grafoRest[j]==grafo[i]:
                    if grafo[i+1]>=grafoRest[j+1][0]:
                        ret=0            
                        break

    return ret
    
def obtenerVecinos(solucion, datos):
    ##Obtención de los vecinos
    vecinos = []
    l=len(datos)
    for i in range(l):
        valido=evaluarNodos(solucion[0],datos[i])
        if valido:
            vecinos.append(datos[i])

    ##Obtención del mejor vecino
    #mejorVecino = vecinos[0]
    #mejorLongitud = evaluarSolucion(datos, mejorVecino)
    #for vecino in vecinos:
    #    longitud = evaluarSolucion(datos, vecino)
    #    if longitud < mejorLongitud:
    #       mejorLongitud = longitud
    #        mejorVecino = vecino
    return vecinos

def hillClimbing(datos):
    l=len(datos)
    ##Creamos una solucion aleatoria
    registros = list(range(l))
    solucion = []
    #for i in range(l):
    registro = datos[random.randint(0, len(registros) - 1)]
    solucion.append(registro)
        #ciudades.remove(ciudad)
    grafo = crearGrafo(registro)

    ##Obtenemos los vecinos 
    vecinos = obtenerVecinos(solucion, datos)
    lvec=len(vecinos)
    for i in range(lvec):
        #grafo = mejorarGrafo(grafo,vecinos[i])

    aciertos=0
    for i in range(l):
        valido=contieneGrafo(grafo,datos[i])
        if valido:
            aciertos+=1

    return grafo, aciertos


def ils(inicial, datos):

    iteraciones = 20
    minSol = inicial[0]
    maxAciertos = inicial[1]

    while iteraciones > 0:

        solucion = hillClimbing(datos)
        if solucion[1] > maxAciertos :
            grafo = solucion[0]
            aciertos = solucion[1]
        iteraciones = iteraciones - 1
    return grafo, aciertos
    
def main():

    datos = []
    with open("BD.txt") as f:
        lineas=[linea.strip("\n") for linea in f.readlines()]
        for linea in lineas:
            datos.append(re.split(r":| ",linea))

    aux=datos
    inicial=hillClimbing(datos)
    resultados=[]
    
    for i in range(0,10):
        print(i,"\n")
        for c in range(0,100):
            sol=ils(inicial,datos)
            #resultados.append(sol)
            #suma+=sol[1]
            #if(sol[1]<minDist):
            #    minDist=sol[1]
            #if(sol[1]>maxDist):
            #    maxDist=sol[1]

        #aciertos=distancias.count(minDist)
        resultados.append([i,sol[0], sol[1]])
        i+=1
    with open("Grafos.csv", "w") as file:
        file.write(",".join(["N", "Grafo","Aciertos"]))
        for res in resultados:
                   file.write(",".join(str(e) for e in res)+"\n")







if __name__ == "__main__":
    main()


