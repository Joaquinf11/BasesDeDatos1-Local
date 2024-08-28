LENGTH_CANT_COLUMNAS = 2
LENGTH_NOMBRE_COLUMNA = 16
LENGTH_CARACTERES = 4


LENGTH_COLUMNA = 20 # tamaño de columna, CHEUQEAR creo que se calculaba con alguna de las constantes anteriores.
                    # creo que seria length nombre columna + length caracteres


def generarArchivo():
    cantColumnas=input("Ingrese la cantidad de columnas: ")
    with open('nombrearchivo.txt','w') as archivo:
        archivo.write(cantColumnas.ljust(LENGTH_CANT_COLUMNAS))
        for i in range(int(cantColumnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i}: ").ljust(LENGTH_NOMBRE_COLUMNA))
            archivo.write(input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i}: ").ljust(LENGTH_CARACTERES))

def offsetHeader():
    titulos,caracteres= readHeader()        #Calculo el tamano con la cantidad de columas
    return  LENGTH_CANT_COLUMNAS + (len(caracteres) * LENGTH_COLUMNA)  # puede fallar dijo tusam revisar


def readHeader():
    titulos=[]
    caracteres=[]
    with open('nombrearchivo.txt','r') as archivo:
        cantColumnas=int(archivo.read(LENGTH_CANT_COLUMNAS))
        for i in range(0,cantColumnas):
            titulos.append(archivo.read(LENGTH_NOMBRE_COLUMNA))
            caracteres.append(int(archivo.read(LENGTH_CARACTERES)))
    return titulos,caracteres

def getOffset(index):
    titulos,caracteres=readHeader()
    pos= offsetHeader()


def readByPK(index):
    pos=  getOffset(index) + offsetHeader()
    return readByOfsset(pos)

def readByOffset(pos):
    with open('nombrearchivo.txt','r') as archivo:
        archivo.seek(pos)

    
    

def mostrarArchivo():
    print("---------Info Header--------------------\n")
    with open('nombrearchivo.txt','r') as archivo:
        print(f"Cantidad de columnas: {archivo.read(LENGTH_CANT_COLUMNAS)} \n")
        print(f'Espacio que ocupa el nombre de columna: {LENGTH_NOMBRE_COLUMNA}\n')
        print(f'Espacio que ocupa el dato de la columna: {LENGTH_CARACTERES}\n')
        
        
        titulos,caracteres=readHeader()
        print("-----------Columnas----------\n")
        for i in range(0,len(caracteres)):
            print(titulos[i],end="")
        print("")
        print("-----------------------------\n")
        
        # archivo.seek(LENNGTH_LINEA);
        # for i in range(0,2):
        #     mostrar=archivo.read(LENNGTH_LINEA)
        #     print(mostrar + "\n")
#falta que muestre los datos del archivo
# 

 