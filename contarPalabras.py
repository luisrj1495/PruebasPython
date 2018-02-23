fichero1=open("archivo.txt")

palabra1=""
palabra2=""
cont=0
mayor=0
palabraMayor=""

for letra in fichero1.read():
    palabra1=palabra1+letra
    if letra==" ":
        cont=0
        fichero2=open("archivo.txt")
        for letra2 in fichero2.read():
            palabra2=palabra2+letra2
            if letra2==" ":
                if palabra1==palabra2:
                    cont=cont+1
                    print cont

                palabra2=""
            fichero2.close()
        if cont>=mayor:
            mayor=cont
            palabraMayor=palabra1
        palabra1=""
        palabra2=""


print "La palabra: "+str(palabraMayor)+" Se repite: "+str(mayor)+" veces!"
