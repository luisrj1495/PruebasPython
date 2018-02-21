contador=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n=0
fichero= open("archivo.txt")
abecedario="abcdefghijklmnopkrstuvwxyz"
for palabra in fichero.read():
    if palabra.lower()=="a":
        contador[0]=contador[0]+1
    elif palabra.lower()=="b":
        contador[1]=contador[1]+1
    elif palabra.lower()=="c":
        contador[2]=contador[2]+1
    elif palabra.lower()=="d":
        contador[3]=contador[3]+1
    elif palabra.lower()=="e":
        contador[4]=contador[4]+1
    elif palabra.lower()=="f":
        contador[5]=contador[5]+1
    elif palabra.lower()=="g":
        contador[6]=contador[6]+1
    elif palabra.lower()=="h":
        contador[7]=contador[7]+1
    elif palabra.lower()=="i":
        contador[8]=contador[8]+1
    elif palabra.lower()=="j":
        contador[9]=contador[9]+1
    elif palabra.lower()=="k":
        contador[10]=contador[10]+1
    elif palabra.lower()=="l":
        contador[11]=contador[11]+1
    elif palabra.lower()=="m":
        contador[12]=contador[12]+1
    elif palabra.lower()=="n":
        contador[13]=contador[13]+1
    elif palabra.lower()=="o":
        contador[14]=contador[14]+1
    elif palabra.lower()=="p":
        contador[15]=contador[15]+1
    elif palabra.lower()=="q":
        contador[16]=contador[16]+1
    elif palabra.lower()=="r":
        contador[17]=contador[17]+1
    elif palabra.lower()=="s":
        contador[18]=contador[18]+1
    elif palabra.lower()=="t":
        contador[19]=contador[19]+1
    elif palabra.lower()=="u":
        contador[20]=contador[20]+1
    elif palabra.lower()=="v":
        contador[21]=contador[21]+1
    elif palabra.lower()=="w":
        contador[22]=contador[22]+1
    elif palabra.lower()=="x":
        contador[23]=contador[23]+1
    elif palabra.lower()=="y":
        contador[24]=contador[24]+1
    elif palabra.lower()=="z":
        contador[25]=contador[25]+1

fichero.close()

for letra in abecedario:
    if max(contador)==contador[n]:
        print "La letra mas repetida es: "+ str(letra)+ " con " + str(max(contador))+" repeticiones"
    n=n+1
