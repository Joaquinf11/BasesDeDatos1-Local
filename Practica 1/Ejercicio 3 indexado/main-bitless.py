import ej3bitless
from ej3bitless import *


def mostrarMenu():
    print("\n ABM de Archivo de METADATA \n")
    print("0- Salir\n" +
          "1 - Mostrar archivo\n" +
          "2 - Alta\n" + 
          "3 - Modificacion\n" +
          "4 - Baja\n")


def main():
    print("Bienvenido al Sistema\n     Altas/Bajas/Modificaciones J.N.E\n")
    
    print("0- Salir\n" +
        "1 - Generar archivo nuevo \n" +
        "2 - Manipular archivo existente\n")
    
    accion=input("Elija una opcion:"  )
    if accion == '0':
        return
    if accion == '1':
            ej3bitless.ingresarNombreArchivo()
            ej3bitless.generarArchivo()
            print("Archivo generado exitosamente.")
    if accion == '2':
        ej3bitless.ingresarNombreArchivo()
        ej3bitless.readHead()
    
    mostrarMenu()
    accion= input("Ingrese una opcion: ")
    while(accion != '0'):
        if accion == '1':
           
                ej3bitless.mostrarArchivo()
            
        elif accion == '2':
           
                print("Ingrese los datos")
                datos= ej3bitless.ingresarDatos()
                ej3bitless.alta(datos)
                print("Alta generada exitosamente.")
            
                
        elif accion == '3':
           
                pk=input("Ingrese la pk que desea modificar: ")
                print("Ingrese los datos")
                datos= ej3bitless.ingresarDatos()
                ej3bitless.update(pk, datos)
                print("Modificacion generada exitosamente.")
           
                
        elif accion == '4':
                pk=input("Ingrese la pk que desea eliminar: ")
                ej3bitless.delete(pk)
                print("Registro eliminado exitosamente.")
    
        mostrarMenu()
        accion=input("Ingrese una opcion:")

main()




