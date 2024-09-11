import ej3_indexado

def mostrarMenu():
    print("\n ABM de Archivo de Metadata \n")
    print("0- Salir\n" +
          "2 - Mostrar archivo\n" +
          "3 - Alta\n" + 
          "4 - Modificacion\n" +
          "5 - Baja\n")

def main():
    print("0- Salir\n" +
        "1 - Generar archivo nuevo \n" +
        "2 - Manipular archivo existente\n")
    
    accion=input("Elija una opcion:"  )
    if accion == '0':
        return
    if accion == '1':
       
            ej3_indexado.generarArchivo()
            print("Archivo generado exitosamente.")
       
            return

    mostrarMenu()
    accion= input("Ingrese una opcion: ")

    ej3_indexado.readHead()

    while(accion != '0'):
        if accion == '2':
           
                ej3_indexado.mostrarArchivo()
            
        elif accion == '3':
           
                print("Ingrese los datos")
                datos= ej3_indexado.ingresarDatos()
                ej3_indexado.insert(None, datos)
                print("Alta generada exitosamente.")
            
                
        elif accion == '4':
           
                index=input("Ingrese el indice que desea modificar: ")
                print("Ingrese los datos")
                datos= ej3_indexado.ingresarDatos()
                ej3_indexado.update(index, datos)
                print("Modificacion generada exitosamente.")
           
                
        elif accion == '5':
                index=input("Ingrese el indice que desea eliminar: ")
                ej3_indexado.delete(index)
                print("Registro eliminado exitosamente.")
        
        
        mostrarMenu()
        accion=input("Ingrese una opcion:")

main()