#Agarramos el archivo:

fname=input('Inserte el nombre del archivo: ')
try:
    fhandler=open(fname)
except:
    print('No se pudo abrir el archivo ...')
    exit()

#Creo el diccionario en el que vamos a almacenar las letras
freq=dict()

#Vamos a tener que recorrer linea por linea, dividir en palabras e iterar palabra por palabras

for line in fhandler:
    words=line.split()
    for word in words:
        count=0
        index=0
        while(count < len(word)):
            if(word[count].isalpha()):
                letra=word[count].lower()
                freq[letra]=freq.get(letra ,0) + 1
                index+=1
            count+=1
#ordenamos bien el diccionario
freqLst=list()

for key,value in freq.items():
    freqLst.append((value,key))
#sorteamos la lista

freqLst.sort(reverse=True)

#imprimimos

for value, key in freqLst:
    print(key,value)
