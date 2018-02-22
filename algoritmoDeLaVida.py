import random


# La mas sencilla e intuitiva
matriz = []
numero_filas=5
numero_columnas=5
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(random.randint(0, 1))
    print matriz[i]
