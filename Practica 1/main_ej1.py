import ejericio1


       
print("El programa ha comenzado.") 
accion= input("Bienvenido seleccione una opcion: A(alta) | B(baja) | M(modificar) | S(salir): ")

while(accion.upper != 'S'):
    if accion.upper() == 'A':
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        codigo =input("Ingrese codigo: ")
        ejericio1.alta(apellido,nombre,codigo)
    elif accion.upper() == 'B':
        indice=int(input('Ingrese el indice que desea eliminar: '))
        ejericio1.baja(indice)
    elif accion.upper() == 'M':
        indice=int(input('Ingrese el indice que desea eliminar: '))
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        codigo =input("Ingrese codigo: ")
        ejericio1.modificar(indice,apellido,nombre,codigo)
    else:
        print("Opción no válida.")
        break;
    accion= input("Bienvenido seleccione una opcion: A(alta) | B(baja) | M(modificar) | S(salir): ")


