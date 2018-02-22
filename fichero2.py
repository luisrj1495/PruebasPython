
n=0
fichero1= open("archivo.txt")
contenido=fichero1.read();
abecedario="abcdefghijklmnopqrstuvwxyz"

cont=0
mayor=0
letraMayor=""

for letra1 in abecedario:
    cont=0
    for letra2 in contenido:
        print letra1 +" "+letra2
        if letra1==letra2:
            print cont
            cont=cont+1
        if cont>=mayor:
            mayor=cont
            letraMayor=letra1


print "La letra mayor es: "+str(letraMayor) + " con: "+ str(mayor) + " repeticiones!"
