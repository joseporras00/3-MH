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

def unicoRegistro(registro1, datos):
    unico=True
    nodos1=registro1[::2]
    while unico==True:
        for m in range(len(datos)):
            nodos2=datos[m][::2]
            if len(nodos1)==len(nodos2):
                cont=0
                aux=nodos2
                for i in range(len(nodos1)):
                    for j in range(i+1,len(nodos2)):
                        if(nodos1[i] == nodos2[j]):
                            nodos2.pop(j)
                            nodos1.pop(i)
                            break

                if len(nodos1)!=cont:
                    unico=False

    return unico


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


def evaluarRestricciones(grafo, registro):

    #Consigue los nodos del grafo y el registro
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
    for i in range(len(datos)):
        if(evaluarNodos(grafo, datos[i])):
            if(evaluarRestricciones(grafo, datos[i])):
                aciertos+=1

    return aciertos
    

def hillClimbing(registro,datos):
    #l=len(datos)
    ##Creamos una solucion aleatoria
    #registros = list(range(l))
    #registro = datos[random.randint(0, len(registros) - 1)]
    grafo = crearGrafo(registro)

    ##Mejoramos el grafo
    aciertos=0
    for i in range(len(datos)):
        if(evaluarNodos(grafo, datos[i])):
            grafo=adaptarGrafo(grafo,datos[i])
            aciertos+=1
        

    #aciertos=evaluarGrafo(grafo,datos)

    return grafo, aciertos


def ils(inicial, datos):

    iteraciones = 20
    grafoSol = inicial[0]
    maxAciertos = inicial[1]

    while iteraciones > 0:

        solucion = hillClimbing(datos)
        if solucion[1] > maxAciertos :
            grafo = solucion[0]
            aciertos = solucion[1]
        iteraciones = iteraciones - 1
    return grafo, aciertos
    
def main():

    datos=leerDatos()

    resultados=[]
    datos2=[]
    datos3=[]
    print(len(datos))

    for i in range(len(datos)):
        if len(datos[i])>=8:
            datos2.append(datos[i])

    print(len(datos2))
    
    for i in range(100):
        print(i,"\n")
        sol=hillClimbing(datos2[i],datos2)


        resultados.append([i,sol[0], sol[1]])
        i+=1
    with open("Grafos.csv", "w") as file:
        file.write(",".join(["N", "Grafo","Aciertos"]))
        for res in resultados:
                   file.write(",".join(str(e) for e in res)+"\n")







if __name__ == "__main__":
    main()

