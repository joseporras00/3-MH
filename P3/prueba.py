import re

datos = []
with open("BD.txt") as f:
    lineas=[linea.strip("\n") for linea in f.readlines()]
    for linea in lineas:
        datos.append(re.split(":| ",linea))


print(lineas[0])
print(datos[0])
aux2=datos[1][::2]
aux=datos[2][::2]

print(aux)
print(aux2)


l=len(aux)
l2=len(aux2)
contador=0
for i in range(l):
    print(contador)
    for j in range(l2):
        #print(j,aux2[j])
        if aux[i]==aux2[j]:
            contador=contador+1
            break


print(aux)

grafoRest=datos[2]
l=list(range(len(grafoRest)))
aux=l[1::2]
for i in aux:
    grafoRest[i]=[-99,99]

print(grafoRest)

l=list(range(len(grafoRest)))
aux=l[::2]

grafo=datos[1]
#print(grafo)
l2=list(range(len(grafo)))
aux2=l2[::2]
    
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

print(ret)


#for j in range(l2):
        #if aux[i]==aux2[j]:
            #aux.pop(i)
