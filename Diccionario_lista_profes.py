instructores2557861 = {}

while True:
    print("info de instructores ")
    print("1. Agregar/modificar nombre el instructor ")
    print("2. Buscar: ")
    print("3. Borrar: ")
    print("4. Listar: ")
    print("5. Salir: ")
    

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre_intructor = input("Ingrese el nombre del Instructor: ")
        if nombre_intructor in instructores2557861:
            print("El instructor ya se encuentra registrado.")
            modificar = input("¿Qué desea modificar? (1. Nombre, 2. materia, 3. numero 4. Cancelar): ")
            if modificar == "1":
                nombre_intructor = input("Ingrese el nuevo nombre del instructor: ")
                instructores2557861[nombre_intructor]['nombre'] = nombre_intructor
                print("nombre del instructor modificado correctamente.")
            elif modificar == "2":
                materia = input("Ingrese la nueva materia del instructor: ")
                instructores2557861[nombre_intructor]['materia'] = materia
                print("Materia  modificada correctamente.")
            elif modificar=="3":
                numero = input("Ingrese el nuevo numero del instructor: ")
                instructores2557861[nombre_intructor]['Numero'] = numero
                print("numero modificado correctamente.")
            elif modificar == "4":
                print("Operación cancelada.")
            else:
                print("Opción inválida.")
        else:
            materia = input("Ingrese la materia del instructor: ")
            numero = input("Ingrese el numero del instructor ")
            instructores2557861[nombre_intructor] = {'materia': materia, 'numero': numero}
            print("El instructor se ha registrado correctamente.")
    
    elif opcion == 2:
        texto_busqueda = input("Ingrese el instructor a buscar: ")
        encontradas = [nombre_instructor for nombre_instructor in instructores2557861.keys() if nombre_intructor.startswith(texto_busqueda)]
        if encontradas:
            print("Intructores encontrados:")
            for nombre_intructor in encontradas:
                print(nombre_intructor)
        else:
            print("No se encontraron artículos.")
    
    elif opcion == 3:
        articulo = input("Ingrese el nombre del instructor a borrar: ")
        if articulo in instructores2557861:
            confirmacion = input("¿Está seguro de que desea borrar el instructor? (s/n): ")
            if confirmacion.lower() == "s":
                del instructores2557861[nombre_intructor]
                print("El instructor ha sido borrado correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("El instructor no existe en el diccionario.")
    
    elif opcion == 4:
        if nombre_intructor:
            print("Intructores disponibles:")
            for nombre_intructor, datos in instructores2557861.items():
                print(f"Nombre: {nombre_intructor}")
                print(f"Materia: {datos['materia']}")
                print(f"Numero: {datos['numero']}")
                print()
        else:
            print("No hay intructores registrados.")

    elif opcion == 5:
        print("Hasta luego.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

    
    

