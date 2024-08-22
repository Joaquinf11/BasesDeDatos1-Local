
lenghtApellido = 16
lenghtNombre = 16
lenghtCodigo = 4
totalLenght = 36

def alta(apellido,nombre,codigo):
    with open('nombrearchivo.txt','a') as archivo:
        archivo.write(apellido.ljust(lenghtApellido))
        archivo.write(nombre.ljust(lenghtNombre))
        archivo.write(codigo.ljust(lenghtCodigo))

def leer(indice):
    offset= (indice-1)*totalLenght
    with open('nombrearchivo.txt','r') as archivo:
        archivo.seek(offset)
        apellido=archivo.read(lenghtApellido)
        nombre=archivo.read(lenghtNombre)
        codigo=archivo.read(lenghtCodigo)
    return apellido+nombre+codigo
    

def baja(indice_eliminar):
    archivo=open('practica1/nombrearchivo.txt','r')
    lineas= archivo.read()
    lineas_modificados=lineas[0:(indice_eliminar-1) * totalLenght ]+lineas[indice_eliminar*totalLenght:len(lineas)]    
    archivo.close()

    archivo=open('nombrearchivo.txt','w')
    archivo.write(lineas_modificados)
    archivo.close()

    


def modificar(indice,apellido,nombre,codigo):
    archivo=open('nombrearchivo.txt','r')
    lineas= archivo.read()
    lineas_hasta_modificar=lineas[0:(indice-1) * totalLenght ]
    lineas_despues_modificar=lineas[(indice*totalLenght):len(lineas)]    
    archivo.close()

    archivo=open('nombrearchivo.txt','w')
    archivo.write(lineas_hasta_modificar)
    archivo.write(apellido.ljust(lenghtApellido))
    archivo.write(nombre.ljust(lenghtNombre))
    archivo.write(codigo.ljust(lenghtCodigo))
    archivo.write(lineas_despues_modificar)
    archivo.close()


    
    
