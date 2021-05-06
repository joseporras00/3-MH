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
                if(int(valores[j])-int(valores[i]) > 0):
                    fila2.append([0, int(valores[j])-int(valores[i])])
                else:
                    fila2.append([int(valores[j])-int(valores[i]), 0])
            else:
                fila2.append([0,0])
        grafo.append(fila2)

    return grafo

def main():

    datos=leerDatos()
    
    grafo=crearGrafo(datos[0])

    print("Registro: ", datos[0], "\nRegistro2: ", datos[28])


    registro2=datos[28]
    restricciones=sacarRestricciones(registro2)


    #Conseguir nodos del grafo mejorado
    nodos1=[]
    for i in range(len(grafo[0])):
        if(grafo[0][i] != 0):
            nodos1.append(grafo[0][i])
    nodos2=registro2[::2]
    nodosFinal=nodos1

    aux=nodos2
    for i in range(len(nodos1)):
        for j in range(len(aux)):
            if(nodos1[i] == aux[j]):
                aux[j]=0
                break
    for i in range(len(aux)):
        if(aux[i] != 0):
            nodosFinal.append(aux[i])

    #Actualizar restricciones del grafo
    print(grafo)
    
    print("\n",restricciones)
    for m in grafo[1][2]:
        print(m)
    #print(range(1,len(grafo)))
    #print(len(grafo[1]))
    for i in range(1,len(grafo)):
        for j in range(1,len(grafo[i])):
            ind1 = grafo[0][i]
            ind2 = grafo[j][0]
            print(i,j,ind1,ind2)
            for k in range(1,len(restricciones)):
                for l in range(1,len(restricciones[k])):
                    if(k != l):
                        if(restricciones[0][k]==ind1 and restricciones[l][0]==ind2):
                            for m in grafo[i][j]:
                                if(restricciones[k][l] != m):
                                    if(restricciones[k][l]>0 and grafo[i][j][1]<restricciones[k][l]):
                                        grafo[i][j]=[grafo[i][j][0], restricciones[k][l]]
                                    else:
                                        if(restricciones[k][l]<0 and grafo[i][j][0]>restricciones[k][l]):
                                            grafo[i][j]=[restricciones[k][l],grafo[i][j][len(grafo[i][j])-1]] 


    print(grafo)



    

if __name__ == "__main__":
    main()
    cls()
