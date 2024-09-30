import os.path
import math

LENGTH_CANT_COLUMNAS = 2
LENGTH_NOMBRE_COLUMNA = 16
LENGTH_CARACTERES = 4
LENGTH_COLUMNA = LENGTH_NOMBRE_COLUMNA + LENGTH_CARACTERES  # tamaño de columna

LENGTH_PUNTERO= 4

PADDING=" "

PATH_ARCHIVO=''

class Metadata:
    cantidad_columnas : int
    titulos= []
    caracteres= []
    size_data : int
    size_head : int
    size_index :int
    size_pk :int

    def __init__(self):
        self.cantidad_columnas= 0
        self.titulos= []
        self.caracteres=[]
        self.size_data= 0 
        self.size_head=0

METADATA = Metadata()

class Index:
    pk =None
    puntero : int

    def __init__(self,pk,puntero):
        self.pk=pk
        self.puntero=puntero
 
def generarArchivo():
    PATH_ARCHIVO=input("Ingrese el nombre del archivo ")
    cantidad_columnas=input("Ingrese la cantidad de columnas: ")
    with open(PATH_ARCHIVO,'w') as archivo:
        archivo.write(cantidad_columnas.ljust(LENGTH_CANT_COLUMNAS,PADDING))
        for i in range(int(cantidad_columnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i}: ").ljust(LENGTH_NOMBRE_COLUMNA,PADDING))
            caracteres=input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i}: ")
            if i== 0:
                METADATA.size_index= caracteres + LENGTH_PUNTERO
                METADATA.size_pk=caracteres
            archivo.write(caracteres.ljust(LENGTH_CARACTERES,PADDING))

def readHead(): 
    with open(PATH_ARCHIVO,'r') as archivo:
        cantidad_columnas=int(archivo.read(LENGTH_CANT_COLUMNAS))
        METADATA.cantidad_columnas=cantidad_columnas  
        METADATA.size_head= LENGTH_CANT_COLUMNAS + (LENGTH_COLUMNA * (int(cantidad_columnas)))
        for i in range(0,cantidad_columnas):
            METADATA.titulos.append(archivo.read(LENGTH_NOMBRE_COLUMNA))
            caracteres=int(archivo.read(LENGTH_CARACTERES))
            METADATA.caracteres.append(caracteres)
            METADATA.size_data +=  caracteres

def readIndex(pos):
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        pk=archivo.read(METADATA.size_pk)
        puntero= archivo.read(LENGTH_PUNTERO)
        return Index(pk,puntero)

def getOffset(pk):
    eOF = os.path.getsize(PATH_ARCHIVO)
    inferior = METADATA.size_head
    superior= eOF
    cantidad_registros = (superior - inferior) / (METADATA.size_data + METADATA.size_index)
    actual = math.floor(cantidad_registros / 2) * (METADATA.size_data + METADATA.size_index) + METADATA.size_head
    index = readIndex(actual) # indice del dato del medio

    while index.pk != pk:
        if pk < index.pk:
            superior = actual
        else:
            inferior = actual + METADATA.size_data + METADATA.size_index

        cantidad_registros = (superior - inferior) / (METADATA.size_data + METADATA.size_index)

        if cantidad_registros == 0:
            return  None

        actual = math.floor(cantidad_registros / 2) * (METADATA.size_data + METADATA.size_index) + inferior
        index = readIndex(actual)
    return int(index.puntero)

def readByPK(pk):
    pos= getOffset(pk)
    return readByOffset(pos)

def readByOffset(pos):
    datos=[]
    with open(PATH_ARCHIVO,'r') as archivo:
        archivo.seek(pos)
        for i in range(0,METADATA.cantidad_columnas):
            datos.append(archivo.read(METADATA.caracteres[i]))
    return datos

def writeByPK(pk,datos):
    if pk is not None:
        pos = getOffset(pk)
    else:
        pos = None
    writeByOffset(pos,datos)

def updateIndex():
    pos= METADATA.size_head
    index_ant=readIndex(pos)
    index = None
    with open (PATH_ARCHIVO,'r+'):
        if index == None:
            archivo.seek(pos + METADATA.size_data + )

def writeNewIndex(pk,puntero):
    with open(PATH_ARCHIVO,'a')as archivo:
        archivo.write(pk.ljust(METADATA.size_pk,PADDING))
        archivo.write(puntero.ljust(LENGTH_PUNTERO,PADDING))
    updateIndex()

def writeByOffset(pos,datos):
    if pos is None:
        pos= os.path.getsize(PATH_ARCHIVO)
        writeNewIndex(datos[0],pos)
    with open(PATH_ARCHIVO,'r+b') as archivo:
        if pos is None:
            archivo.seek(0,2)
        else:
            archivo.seek(pos)
        for i in range(0, METADATA.cantidad_columnas):
            archivo.write(datos[i].ljust(METADATA.caracteres[i],PADDING).encode("utf-8"))
    

def insert(index,datos):
    writeByPK(index,datos)

def delete(index):
    pos=getOffset(index)
    with open(PATH_ARCHIVO,'r+') as archivo:
       archivo.seek(pos)



def update(index,new_datos):
    old_datos = readByPK(index)
    if old_datos[0] == "B":
        print("No se encuentra cargado el registro")
        return
    for i in range(0,METADATA.cantidad_columnas-1):
        if new_datos[i].isspace():
            new_datos[i]= old_datos[i+1]
    writeByPK(index,new_datos)

def mostrarArchivo():
    print("----------------------------------Head------------------------------\n")
    for i in range(1,METADATA.cantidad_columnas):
        print(f"Columna {i}: {METADATA.titulos[i]}  || Longitud: {METADATA.caracteres[i]}") 
    print("----------------------------------------------------------------------\n")

    index=1
    while True:
        datos=readByPK(index)
        if datos[0] == "":
            break
        elif datos[0] == "B":
            index +=1
        else:
            print("-----------------------------")
            for i in range(1,METADATA.cantidad_columnas):
                    print(f"{METADATA.titulos[i].strip()}: {datos[i]}")
            index+=1
            print("-----------------------------\n")

def ingresarDatos():
    datos = []
    for i in range(1,METADATA.cantidad_columnas):
        datos.append(input(f"{METADATA.titulos[i].strip()}: ").ljust(METADATA.caracteres[i],PADDING))
    return datos