import random
import math
import re

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
    nodos1=grafo[0][1::]
    nodos2=registro[::2]
    cont=0
    for i in range(len(nodos1)):
        for j in range(len(nodos2)):
            if(nodos1[i] == nodos2[j]):
                nodos2.pop(j)
                cont+=1
                break

    if cont==len(nodos1):
        return True
    else:
        return False




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

    
    

def iniciar(registro,datos):
    grafo = crearGrafo(registro)

    ##Mejoramos el grafo y sacamos respectivos aciertos
    aciertos=0
    for i in range(len(datos)):
        if(evaluarNodos(grafo, datos[i])):
            grafo=adaptarGrafo(grafo,datos[i])
            aciertos+=1
        

    return grafo, aciertos

def ils(datos):
    maxAciertos=0
    grafo=[]
    for i in range(len(datos)):
        print(i)
        sol=iniciar(datos[i],datos)
        if sol[1]>maxAciertos:
            grafo=sol[0]
            maxAciertos=sol[1]
    return grafo, maxAciertos
    
    
def main():

    datos=leerDatos()

    resultados=[]
    datos2=[]
    print(len(datos))

    for i in range(len(datos)):
        if len(datos[i])>=8:
            datos2.append(datos[i])

    #inicial=iniciar(datos2[0],datos2)
    sol=ils(datos2)
    resultados.append([0,sol[0], sol[1]])
    
    with open("GrafosTodos2.csv", "w") as file:
        file.write(",".join(["N", "Grafo","Aciertos"]))
        for res in resultados:
                   file.write(",".join(str(e) for e in res)+"\n")







if __name__ == "__main__":
    main()

