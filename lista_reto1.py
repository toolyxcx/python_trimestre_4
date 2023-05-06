instructores = []

while True:
    print("Opciones disponibles:")
    print("1. Agregar un instructor a la lista")
    print("2. Listar los instructores")
    print("3. Modificar un instructor")
    print("4. Borrar un instructor")
    print("5. Buscar un instructor")
    print("6. Ordenar la lista de instructores")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        instructor = input("Ingrese el nombre del instructor: ")
        instructores.append(instructor)
        print("Instructor agregado a la lista.")
    
    elif opcion == "2":
        print("Instructores en la lista:")
        for index, instructor in enumerate(instructores):
            print(index, instructor)

    elif opcion == "3":
        if len(instructores) == 0:
            print("La lista de instructores está vacía.")
        else:
            for index, instructor in enumerate(instructores):
                print(index, instructor)
            index_modificar = int(input("Ingrese el índice del instructor a modificar: "))
            if index_modificar < 0 or index_modificar >= len(instructores):
                print("Índice inválido.")
            else:
                nuevo_instructor = input("Ingrese el nuevo nombre del instructor: ")
                instructores[index_modificar] = nuevo_instructor
                print("Instructor modificado.")
    
    
    elif opcion == "4":
        if len(instructores) == 0:
            print("La lista de instructores está vacía.")
        else:
            for index, instructor in enumerate(instructores):
                print(index, instructor)
            index_borrar = int(input("Ingrese el índice del instructor a borrar: "))
            if index_borrar < 0 or index_borrar >= len(instructores):
                print("Índice inválido.")
            else:
                instructor_borrar = instructores.pop(index_borrar)
                print("Se ha borrado el instructor:", instructor_borrar)

    elif opcion == "5":
        if len(instructores) == 0:
            print("La lista de instructores está vacía.")
        else:
            nombre_buscar = input("Ingrese el nombre del instructor a buscar: ")
            encontrado = False
            for instructor in instructores:
                if nombre_buscar.lower() == instructor.lower():
                    print("El instructor", instructor, "se encuentra en la lista.")
                    encontrado = True
                    break
            if not encontrado:
                print("El instructor no se encuentra en la lista.")
    
    elif opcion == "6":
        instructores.sort()
        print("La lista de instructores ha sido ordenada de A-Z.")
        for index, instructor in enumerate(instructores):
            print(index, instructor)
    
    elif opcion == "7":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")



    
            
        