def alta(apellido,nombre,codigo):
    with open('nombrearchivo.txt','a') as archivo:
        archivo.writelines([apellido + "\t",nombre + "\t",codigo+"\n"])


def baja(indice_eliminar):
    archivo=open('nombrearchivo.txt','r')
    lineas= archivo.readlines()
    
    lineas_modificadas= lineas[0:indice_eliminar-1] + lineas[indice_eliminar:len(lineas)]
    
    archivo.close()

    archivo=open('nombrearchivo.txt','w')
    archivo.writelines(lineas_modificadas)
    archivo.close()

def modificar(indice,apellido,nombre,codigo):
    archivo=open('nombrearchivo.txt','r')
    lineas= archivo.readlines()
    lineas_hasta_modificar=lineas[0:(indice-1) ]
    lineas_despues_modificar=lineas[(indice):len(lineas)]    
    archivo.close()

    archivo=open('nombrearchivo.txt','w')
    archivo.writelines(lineas_hasta_modificar)
    archivo.writelines([apellido + "\t",nombre + "\t",codigo+"\n"])
    archivo.writelines(lineas_despues_modificar)
    archivo.close()


    


