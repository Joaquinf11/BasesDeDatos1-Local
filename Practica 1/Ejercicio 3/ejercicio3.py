LENGTH_CANT_COLUMNAS = 2
LENGTH_NOMBRE_COLUMNA = 16
LENGTH_CARACTERES = 4


LENGTH_COLUMNA = LENGTH_NOMBRE_COLUMNA + LENGTH_CARACTERES  # tamaño de columna

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
    return size_data    

def getOffset(index):
    size_header=lengthHeader()
    size_data= lenghData()
    pos= size_header + (size_data * ((int(index))-1))
    return pos


def readByPK(index):
    pos= getOffset(index)
    return readByOffset(pos)

def readByOffset(pos):
    titulos,caracteres=readHeader()
    datos=[]
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        for i in range(0,len(caracteres)):
            datos.append(archivo.read(caracteres[i]))
    return datos

def writeByPK(index,datos):
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
    writeByPK(index,datos)

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

def update(index,new_datos):
    #old_datos = readByPK(index). FALTARIA preguntar si alguno de los datos nuevos es none para reemplazarlo por el old correspondiente
    writeByPK(index,new_datos)

def mostrarArchivo():
    # print("---------------------------Info Header---------------------------\n")
    # with open(PATH_ARCHIVO,'r') as archivo:
    #     print(f"Cantidad de columnas: {archivo.read(LENGTH_CANT_COLUMNAS)} \n")
    #     print(f'Espacio que ocupa el nombre de columna: {LENGTH_NOMBRE_COLUMNA}\n')
    #     print(f'Espacio que ocupa el dato de la columna: {LENGTH_CARACTERES}\n')
    #     print("-----------------------------------------------------------------\n")
        
        titulos,caracteres=readHeader()
        print("----------------------------------HEADER------------------------------\n")
        for i in range(0,len(caracteres)):
            print(f"Columna {i}: {titulos[i].strip()}  || Longitud: {caracteres[i]}") 
        print("----------------------------------------------------------------------\n")

        
        index=1
        while True:
            datos=readByPK(index)
            if datos[0] == "":
                break
            print("-----------------------------")
            for i in range(0,len(datos)):
                    print(f"{titulos[i].strip()}: {datos[i]}")
            index+=1
        print("-----------------------------\n")

def ingresarDatos():
    titulos,caracteres= readHeader()
    datos = []
    for i in range(len(caracteres)):
        datos.append(input(f"{titulos[i].strip()}: ").ljust(caracteres[i]))
    return datos