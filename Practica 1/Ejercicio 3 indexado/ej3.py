import math
import os.path
from math import trunc
from os import system

global PATH
PATH = ''
LENGTH_CANT_COLUMNAS = 2
LENGTH_TITULO = 16
LENGTH_CARACTERES = 4
LENGTH_COLUMNA = LENGTH_TITULO + LENGTH_CARACTERES
LENGTH_PUTNERO = 4
PADDING = " "
global METADATA
METADATA= None

class Metadata:
    cantidadColumnas : int
    titulos = []
    caracteres = []
    lenghtDato : int
    root_index : int
    lenghtIndexEntry : int

    def __init__(self):
        cantidadColumnas = 0
        titulos = []
        caracteres = []
        lenghtDato = 0
        root_index = 0
        lenghtIndexEntry = 0

    def caracteres_pk(self):
        if self.caracteres is None or len(self.caracteres) == 0:
            return None

        return self.caracteres[0]

    def titulos_pk(self):
        if self.titulos is None or len(self.titulos) == 0:
            return None

        return self.titulos[0]



class IndexEntry:
    pk = None
    puntero : int
    posicion : int

    def __init__(self, pk,puntero,posicion = 0):
        self.pk = pk
        self.puntero = puntero
        self.posicion = posicion

    def isPK(self,pk):
        return self.pk == pk

    def next(self):
        return readIndex(self.posicion + METADATA.lenghtIndexEntry + METADATA.lenghtDato)

    def hasNext(self):
        return self.next().pk != ""

    def readDato(self):
        return readByOffset(self.puntero)

    def write(self):
        with open(PATH,"r+") as archivo:
            archivo.seek(self.posicion)
            archivo.write(str(self.pk).ljust(METADATA.caracteres_pk(),PADDING))
            archivo.write(str(self.puntero).ljust(LENGTH_PUTNERO,PADDING))


class Dato:
    datos = None

    def __init__(self):
        self.datos = []

    def pk(self):
        if self.datos is None or len(self.datos) == 0:
            return None

        return self.datos[0]
    
def ingresarNombreArchivo():
    global PATH
    PATH= input("Ingrese el nombre del archivo: ") + ".txt"
   
def ingresarDatos(pk = None):
    dato = Dato()
    j = 0
    if pk is not None:
        j = 1
        dato.datos.append(pk.ljust(METADATA.caracteres_pk(),PADDING))
    for i in range(j,METADATA.cantidadColumnas):
        dato.datos.append(input(f"{METADATA.titulos[i].strip()}: ").ljust(METADATA.caracteres[i],PADDING))
    return dato

def generarArchivo():
    cantidad_columnas = input("numero de columnas: ")
    with open(PATH,"wt") as archivo:
        archivo.write(cantidad_columnas.ljust(LENGTH_CANT_COLUMNAS,PADDING))
        for i in range(int(cantidad_columnas)):
            archivo.write(input(f"inserte el titulo de la columna numero {i + 1}: ").ljust(LENGTH_TITULO,PADDING))
            archivo.write(input(f"inserte la cantidad de caracteres utilizados por dato en la columna numero {i + 1}: ").ljust(LENGTH_CARACTERES,PADDING))
    readHead()
    
def readHead():
    global METADATA
    METADATA = Metadata()
    file = open(PATH, "r")
    METADATA.cantidadColumnas = int(file.read(LENGTH_CANT_COLUMNAS))
    for i in range(METADATA.cantidadColumnas):
        METADATA.titulos.append(file.read(LENGTH_TITULO))
        METADATA.caracteres.append(int(file.read(LENGTH_CARACTERES)))
    METADATA.lenghtIndexEntry = METADATA.caracteres_pk() + LENGTH_PUTNERO
    METADATA.root_index = LENGTH_CANT_COLUMNAS + (LENGTH_COLUMNA * METADATA.cantidadColumnas)  # salto el header
    file.close()

    resultado = 0
    for i in range(METADATA.cantidadColumnas):
        resultado += METADATA.caracteres[i]
    METADATA.lenghtDato = resultado
    
def getOffset(pk):
    eOF = os.path.getsize(PATH)
    header = METADATA.cantidadColumnas + METADATA.cantidadColumnas * LENGTH_COLUMNA
    inferior = header
    superior= eOF
    canRegistros = (superior - inferior) / (METADATA.lenghtDato + METADATA.lenghtIndexEntry)
    actual = math.floor(canRegistros / 2) * (METADATA.lenghtDato + METADATA.lenghtIndexEntry) + header
    index = readIndex(actual) # indice del dato del medio

    while index.pk != pk:
        if pk < index.pk:
            superior = actual
        else:
            inferior = actual + METADATA.lenghtDato + METADATA.lenghtIndexEntry

        canRegistros = (superior - inferior) / (METADATA.lenghtDato + METADATA.lenghtIndexEntry)

        if canRegistros == 0:
            return  None

        actual = math.floor(canRegistros / 2) * (METADATA.lenghtDato + METADATA.lenghtIndexEntry) + inferior
        index = readIndex(actual)
    return int(index.puntero)

def readByOffset(offset):
    with open(PATH, "rt") as archivo:
        archivo.seek(int(offset))
        dato = Dato()

        for caracteres in METADATA.caracteres:
            dato.datos.append(archivo.read(caracteres))
    return dato

def readIndex(offset):
    with open(PATH, "rt") as archivo:
        archivo.seek(offset)
        pk = archivo.read(METADATA.caracteres_pk())
        puntero = archivo.read(LENGTH_PUTNERO)
    return IndexEntry(pk, puntero, offset)

def readByPK(pk):
    return readByOffset(getOffset(pk))

def write(dato):
    with open(PATH,"at") as archivo:
        for i in range (METADATA.cantidadColumnas):
            archivo.write(dato.datos[i].ljust(METADATA.caracteres[i],PADDING))

def updateIndex(newIndex):
    posicion = METADATA.root_index
    for i in range(len(newIndex)):
        newIndex[i].posicion = posicion
        newIndex[i].write()
        posicion += METADATA.lenghtIndexEntry + METADATA.lenghtDato

def update(pk,dato):
    offset = getOffset(pk)
    with open(PATH,"r+b") as archivo:
        archivo.seek(offset)

        archivo.seek(METADATA.caracteres_pk(),1)

        for i in range (1,METADATA.cantidadColumnas):
            archivo.write(dato.datos[i].ljust(METADATA.caracteres[i],PADDING).encode("utf-8"))

def delete(pk):
    pk= pk.ljust(METADATA.caracteres_pk(),PADDING)
    puntero = getOffset(pk)
    eOF = os.path.getsize(PATH)

    index = readIndex(METADATA.root_index)
    newIndex = []



    with open(PATH,"r+") as file:
        file.seek(eOF - METADATA.lenghtDato)
        ultimoRegistro = file.read(METADATA.lenghtDato)

        if index.pk != pk:
            newIndex.append(index)
            if index.pk == ultimoRegistro[:METADATA.caracteres_pk()]:
                index.puntero = puntero

        while index.hasNext():
            index = index.next()
            if index.pk != pk:

                if index.pk == ultimoRegistro[:METADATA.caracteres_pk()]:
                    index.puntero = puntero

                newIndex.append(index)

        file.seek(puntero)
        file.write(ultimoRegistro)
        file.seek(eOF - METADATA.lenghtDato - METADATA.lenghtIndexEntry)
        file.truncate()

    updateIndex(newIndex)

def alta(dato):
    eOF = os.path.getsize(PATH)
    new_index = IndexEntry(dato.pk(), eOF + METADATA.lenghtIndexEntry)

    index = readIndex(METADATA.root_index)
    agregue = False

    if index.pk != "":
        if new_index.pk < index.pk:
            indexs = [new_index,index]
            agregue = True
        else:
            indexs = [index]

        while index.hasNext():

            index = index.next()

            if not agregue and new_index.pk < index.pk:
                indexs.append(new_index)
                agregue = True

            indexs.append(index)
    else:
        indexs = [new_index]
        agregue = True

    if not agregue:
        indexs.append(new_index)

    with open(PATH,"at") as f:
        f.write("".ljust(METADATA.lenghtIndexEntry))

    updateIndex(indexs)
    write(dato)



def mostrarArchivo():
    for i in range(METADATA.cantidadColumnas):
        print(METADATA.titulos[i].ljust(METADATA.caracteres[i] if METADATA.caracteres[i] > LENGTH_TITULO else LENGTH_TITULO,PADDING),end="")
    print("")
    index = readIndex(METADATA.root_index)

    if index.pk != "":
        dato = index.readDato()
        for i in range(METADATA.cantidadColumnas):
            print(dato.datos[i].ljust(METADATA.caracteres[i] if METADATA.caracteres[i] > LENGTH_TITULO else LENGTH_TITULO,PADDING),end="")
        print("")
        while index.hasNext():
            index = index.next()
            dato = index.readDato()
            for i in range(0,METADATA.cantidadColumnas):
                print(dato.datos[i].ljust(METADATA.caracteres[i] if METADATA.caracteres[i] > LENGTH_TITULO else LENGTH_TITULO,PADDING),end="")
            print("")



    
 