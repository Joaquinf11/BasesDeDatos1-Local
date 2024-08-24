
# LENGTHAPELLIDO = 16
# LENGTHNOMBRE = 16
# LENGTHCODIGO = 4
# TOTALLENGTH = 36
# CARACTERRELLENO= " "

# def alta(apellido,nombre,codigo):
#     with open('nombrearchivo.txt','a') as archivo:
#         archivo.write(apellido.ljust(LENGTHAPELLIDO, CARACTERRELLENO))
#         archivo.write(nombre.ljust(LENGTHNOMBRE,CARACTERRELLENO))
#         archivo.write(codigo.ljust(LENGTHCODIGO,CARACTERRELLENO))

# def leer(indice):
#     offset= (indice-1)*TOTALLENGTH
#     with open('nombrearchivo.txt','r') as archivo:
#         archivo.seek(offset)
#         apellido=archivo.read(LENGTHAPELLIDO)
#         nombre=archivo.read(LENGTHNOMBRE)
#         codigo=archivo.read(LENGTHCODIGO)
#     return apellido+nombre+codigo
    

# def baja(indice_eliminar):
#     archivo=open('practica1/nombrearchivo.txt','r')
#     lineas= archivo.read()
#     lineas_modificados=lineas[0:(indice_eliminar-1) * TOTALLENGTH ]+lineas[indice_eliminar*TOTALLENGTH:len(lineas)]    
#     archivo.close()

#     archivo=open('nombrearchivo.txt','w')
#     archivo.write(lineas_modificados)
#     archivo.close()

    


# def modificar(indice,apellido,nombre,codigo):
#     archivo=open('nombrearchivo.txt','r')
#     lineas= archivo.read()
#     lineas_hasta_modificar=lineas[0:(indice-1) * TOTALLENGTH ]
#     lineas_despues_modificar=lineas[(indice*TOTALLENGTH):len(lineas)]    
#     archivo.close()

#     archivo=open('nombrearchivo.txt','w')
#     archivo.write(lineas_hasta_modificar)
#     archivo.write(apellido.ljust(LENGTHAPELLIDO))
#     archivo.write(nombre.ljust(LENGTHNOMBRE))
#     archivo.write(codigo.ljust(LENGTHCODIGO))
#     archivo.write(lineas_despues_modificar)
#     archivo.close()


#---------- Corregido en clase, FALTA ARREGLAR LAS LLAMADAS DESDE EL MAIN 
    
from os import write
import os
TAMANIOAPELLIDO = 16
TAMANIONOMBRE = 16
TAMANIOCODIGO = 4
TAMANIODATO= TAMANIOCODIGO + TAMANIOAPELLIDO + TAMANIONOMBRE
PATH = "Archivo.txt"
"""si multiplico 36 por la cantidad de datos,obtengo el tamaño del archivo"""



def readByPK(index):
    pos = offset(index)
    return readByOffset(pos)

def readByOffset(pos):
    with open(PATH,"rt",encoding="utf-8") as archivo:
        archivo.seek(pos)
        apellido = archivo.read(TAMANIOAPELLIDO).strip()
        nombre = archivo.read(TAMANIONOMBRE).strip()
        codigo = archivo.read(TAMANIOCODIGO).strip()
        return apellido,nombre,codigo

def writeByPK(index,apellido,nombre,codigo):
    if index is not None:
        pos = offset(index)
    else:
        pos = None
    writeByOffset(pos,apellido,nombre,codigo)

def writeByOffset(pos,apellido,nombre,codigo):
    with open(PATH,"r+b") as archivo:
        if pos is None:
            archivo.seek(0,2)
        else:
            archivo.seek(pos)
        archivo.write(apellido.ljust(TAMANIOAPELLIDO).encode("utf-8"))
        archivo.write(nombre.ljust(TAMANIONOMBRE).encode("utf-8"))
        archivo.write(codigo.ljust(TAMANIOCODIGO).encode("utf-8"))

def offset(index):
    offset1 = TAMANIODATO * (index-1)
    return offset1


def insert(new_apellido,new_nombre,new_codigo):
    writeByPK(None,new_apellido, new_nombre, new_codigo)

def delete(index):
    #corregido
    pos = offset(index)
    with open(PATH,"r+b") as archivo:
        archivo.seek(-TAMANIODATO,2)
        resto = archivo.read()
        archivo.seek(pos)
        archivo.write(resto)
        archivo.seek(-TAMANIODATO,2)
        archivo.truncate()


def update(index, new_apellido, new_nombre, new_codigo):
    old_apellido,old_nombre,old_codigo = readByPK(index)
    if new_apellido is None:
        new_apellido = old_apellido

    if new_nombre is None:
        new_nombre = old_nombre

    if new_codigo is None:
        new_codigo = old_codigo

    writeByPK(index,new_apellido,new_nombre,new_codigo)



def mostrarArchivo():
    index = 1
    while True:
        apellido,nombre,codigo = readByPK(index)
        if not codigo:
            break
        print("----------------------")
        print("Cliente ", index)
        print("Apellido: ", apellido)
        print("Nombre: ", nombre)
        print("Código: ", codigo)
        print("----------------------")
        index += 1