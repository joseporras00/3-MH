import random
import math
import re

def cls(): print("\n" * 40)

def leerDatos():
    
    datos=[]
    with open("BD.txt") as f:
        lineas=[linea.strip("\n") for linea in f.readlines()]
        for linea in lineas:
            datos.append(re.split(":| ",linea))
    return datos

def sacarRestricciones(registro):

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

def evaluarNodos(grafo, registro):

    nodos1=grafo[0][1:]
    #for i in range(1,len(grafo[0])):
    #    if(grafo[0][i] != 0):
    #        nodos1.append(grafo[0][i])
            
    nodos2=registro[::2]
    cont=0
    for i in range(len(nodos1)):
        for j in range(len(nodos2)):
            if(nodos1[i] == nodos2[j]):
                #nodos2[j]=0
                nodos2.pop(j)
                cont+=1
                break
    #for i in range(len(nodos2)):
    #    if(nodos2[i] != 0):
    #        return False
    #return True
    #print(cont)
    if cont==len(nodos1):
        return True
    else:
        return False

def evaluarRestricciones(grafo, registro):

    #Consigue los nodos del grafo y el registro
    #nodos1=[]
    #for i in range(1,len(grafo[0])):
    #    if(grafo[0][i] != 0):
    #        nodos1.append(grafo[0][i])

    nodos1=grafo[0][1:]
    nodos2=registro[::2]

    #
    restricciones=sacarRestricciones(registro)
    #
    acierto=True
    for i in range(1,len(grafo)):
        for j in range(1,len(grafo[i])):
            if(i != j):
                ind1 = grafo[0][i]
                ind2 = grafo[j][0]
                for k in range(1,len(restricciones)):
                    for l in range(1,len(restricciones[k])):
                        if(k != l):
                            if(restricciones[0][k]==ind1 and restricciones[l][0]==ind2):
                                found=False
                                for m in list(range(grafo[i][j][0],grafo[i][j][1]+1)):
                                    if(restricciones[k][l] == m):
                                        found=True
                                if(found==False):
                                    return False
    return acierto


def crearGrafo(registro):
    
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
                fila2.append([int(valores[j])-int(valores[i]), int(valores[j])-int(valores[i])])
            else:
                fila2.append([0,0])
        grafo.append(fila2)

    return grafo

def adaptarGrafo(grafo, registro):

    if(evaluarNodos(grafo, registro)):
        restricciones = sacarRestricciones(registro)
        for i in range(1,len(grafo)):
            for j in range(1,len(grafo[i])):
                if(i != j):
                    ind1 = grafo[0][i]
                    ind2 = grafo[j][0]
                    for k in range(1,len(restricciones)):
                        for l in range(1,len(restricciones[k])):
                            if(k != l):
                                if(restricciones[0][k]==ind1 and restricciones[l][0]==ind2):
                                    for m in grafo[i][j]:
                                        if(restricciones[k][l] != m):
                                            if(grafo[i][j][1]<restricciones[k][l]):
                                                grafo[i][j][1]= restricciones[k][l]
                                            else:
                                                if(grafo[i][j][0]>restricciones[k][l]):
                                                    grafo[i][j][0]=restricciones[k][l]
    
                                                
    return grafo

def evaluarGrafo(grafo, datos):
    aciertos=0
    evN=0
    for i in range(len(datos)):
        if(evaluarNodos(grafo, datos[i])):
            evN+=1
            if(evaluarRestricciones(grafo, datos[i])):
                aciertos+=1

    return evN,aciertos
            

def main():

    datos=leerDatos()

    
    grafo=crearGrafo(datos[1])
    print(grafo)

    for i in range(len(datos)):
        grafo=adaptarGrafo(grafo,datos[i])

    print(grafo)

    evN,aciertos=evaluarGrafo(grafo, datos)
    print(evN)
    print(aciertos)
    
    
    













    #Conseguir nodos del grafo mejorado
    #nodos1=[]
    #for i in range(len(grafo[0])):
    #    if(grafo[0][i] != 0):
    #        nodos1.append(grafo[0][i])
    #nodos2=registro[::2]
    #nodosFinal=nodos1
    #
    #aux=nodos2
    #for i in range(len(nodos1)):
    #    for j in range(len(aux)):
    #        if(nodos1[i] == aux[j]):
    #            aux[j]=0
    #            break
    #for i in range(len(aux)):
    #    if(aux[i] != 0):
    #        nodosFinal.append(aux[i])


if __name__ == "__main__":
    main()
    #cls()
