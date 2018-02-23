import random

numero_filas=input("Filas")
numero_columnas=input("Columnas")


# La mas sencilla e intuitiva
matriz = []
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(random.randint(0, 1))
    print matriz[i]


#comprobar si la celula esta viva
if matriz[i][j]==1:
    j=j-1
    if j<=-1:
        i=i-1
        if i<=-1:
            j=j+1
            i=i+1
            #Compruebo a la derecha
            if matriz[i][j+1]==1:
                cont1=cont1+1
            else:
                cont0=cont0+1
            #conpruebo hacia abajo
            if matriz[i+1][j]==1:
                cont1=cont1+1
            else:
                cont0=cont0+1
            #




if j>=n or j<=-1:





if matriz[i][j+1]==1:
    cont=cont+1
elif matriz[i][j-1]==1:
    cont=cont+1



print "----"
print matriz[2][1+1]
