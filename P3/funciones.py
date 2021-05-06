#funciones

#No entiendo muy bien como lo hacen
def contieneGrafo(grafo, registro):
    found=false
    currentReg=0

    stack=[]
    for i in range(len(grafo)):
        if(grafo[i][0]==registro[currentReg][0]:
           stack.append([0,i])

    while stack and not found:
        current=stack.pop()
        currentReg=current[0]
        currentNode=grafo[current[1]]

        currentReg+=1
        if(currentReg is len(registro)):
            found=true
        else:
            dif=registro[currentReg][1] - registro[currentReg-1][1]
            for i in range(len(grafo)):
                if grafo[i][0] is registro[currentReg][0]:
                    if diff in currentNode[1][i]:
                        stack.append([currentReg,i])

    return found
