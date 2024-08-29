LENGTH_CANT_COLUMNAS = 2
LENGTH_NOMBRE_COLUMNA = 16
LENGTH_CARACTERES = 4


LENGTH_COLUMNA = 20 # tamaño de columna, CHEUQEAR creo que se calculaba con alguna de las constantes anteriores.
                    # creo que seria length nombre columna + length caracteres

PATH_ARCHIVO= 'nombrearchivo.txt'

def generarArchivo():
    cantColumnas=input("Ingrese la cantidad de columnas: ")
    with open(PATH_ARCHIVO,'w') as archivo:
        archivo.write(cantColumnas.ljust(LENGTH_CANT_COLUMNAS))
        for i in range(int(cantColumnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i}: ").ljust(LENGTH_NOMBRE_COLUMNA))
            archivo.write(input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i}: ").ljust(LENGTH_CARACTERES))

def lengthHeader():
    with open(PATH_ARCHIVO,'r') as archivo:
        cantColumnas=archivo.read(LENGTH_CANT_COLUMNAS)
    size_header= LENGTH_CANT_COLUMNAS + (LENGTH_COLUMNA * (int(cantColumnas)))
    return size_header


def readHeader():
    titulos=[]
    caracteres=[]
    with open(PATH_ARCHIVO,'r') as archivo:
        cantColumnas=int(archivo.read(LENGTH_CANT_COLUMNAS))
        for i in range(0,cantColumnas):
            titulos.append(archivo.read(LENGTH_NOMBRE_COLUMNA))
            caracteres.append(int(archivo.read(LENGTH_CARACTERES)))
    return titulos,caracteres

def lenghData():
    size_data=0
    titulos,caracteres= readHeader()
    for i in range(0,len(caracteres)):
            longitud=(int (caracteres[i]))
            size_data+= longitud
    # with open(PATH_ARCHIVO,'r') as archivo:
    #     cantColumnas=(int(archivo.read(LENGTH_CANT_COLUMNAS)))
    #     for i in range(0,cantColumnas):
    #         longitud=(int (archivo.read(LENGTH_NOMBRE_COLUMNA + LENGTH_CARACTERES)))
    #         size_data+= longitud
    return size_data    

def getOffset(index):
    size_header=lengthHeader()
    size_data= lenghData()
    pos= size_header + (size_data * ((int(index))-1))
    return pos


def readByPK(index):
    pos= getOffset
    return readByOffset(pos)

def readByOffset(pos):
    columnas=[]
    data=[]
    with open(PATH_ARCHIVO,'r') as archivo:
        cantColumnas= int(archivo.read(LENGTH_CANT_COLUMNAS))
        archivo.seek(pos)
        for i in range(0,cantColumnas):
            columnas[i].append(archivo.read(LENGTH_COLUMNA))
            data[i].append(archivo.read(LENGTH_CARACTERES))
    return columnas,data

def writeByPk(index,datos):
    if index is not None:
        pos = getOffset(index)
    else:
        pos = None
    writeByOffset(pos,datos)
    

def writeByOffset(pos,datos):
    titulos,caracteres= readHeader()
    with open(PATH_ARCHIVO,'r+b') as archivo:
        if pos is None:
            archivo.seek(0,2)
        else:
            archivo.seek(pos)
        for i in range(0, len(datos)):
            archivo.write(datos[i].ljust(int(caracteres[i])).encode("utf-8"))  
    

def insert(index,datos):
    writeByPk(index,datos)

def delete(index):
    pos=getOffset(index)
    size_data=lenghData()
    with open(PATH_ARCHIVO,'r+b') as archivo:
        archivo.seek(-size_data,2)
        ultimo_registro= archivo.read(size_data)
        archivo.seek(pos)
        archivo.write(ultimo_registro)
        archivo.seek(-size_data,2)
        archivo.truncate()

def mostrarArchivo():
    print("---------------------------Info Header---------------------------\n")
    with open(PATH_ARCHIVO,'r') as archivo:
        print(f"Cantidad de columnas: {archivo.read(LENGTH_CANT_COLUMNAS)} \n")
        print(f'Espacio que ocupa el nombre de columna: {LENGTH_NOMBRE_COLUMNA}\n')
        print(f'Espacio que ocupa el dato de la columna: {LENGTH_CARACTERES}\n')
        print("-----------------------------------------------------------------\n")
        
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

def ingresarDatos():
    titulos,caracteres= readHeader()
    datos = []
    for i in range(len(caracteres)):
        datos.append(input(f"{titulos[i].strip()}: ").ljust(caracteres[i]))
    return datos