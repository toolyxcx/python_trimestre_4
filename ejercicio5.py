presupuesto = 100000
total = 0

for i in range(5):
    print("Opciones:")
    print("1. Pagar transporte (6000)")
    print("2. Gastarle a tu profe favorita (10000)")
    print("3. Ganar dinero (acumulativo) (5000)")
    
    opcion = int(input("Ingresa el número de tu opción: "))
    
    if opcion == 1:
        presupuesto -= 6000
        print("Has pagado 6000 por transporte")
    elif opcion == 2:
        presupuesto -= 10000
        print("Has gastado 10000 en tu profe favorita")
    elif opcion == 3:
        total += 5000
        print("Has ganado 5000")
    
    print("Tu presupuesto actual es de", presupuesto)
    print("Tu acumulado actual es de", total)

