import random
import math
import re

def sacarRestricciones(registro):

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

def main():

    datos = []
    with open("BD.txt") as f:
        lineas=[linea.strip("\n") for linea in f.readlines()]
        for linea in lineas:
            datos.append(re.split(r":| ",linea))

    grafo=sacarRestricciones(datos[200])

    print(datos[200], "\nGrafo:\n")

    for i in range(len(grafo)):
        print(grafo[i], "\n")
    

if __name__ == "__main__":
    main()
