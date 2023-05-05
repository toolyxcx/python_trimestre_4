presupuesto = 100000
acumulado = 0
gasto_total = 0
repetir = True

while repetir:
    print("Opciones:")
    print("1. Pagar transporte (6000)")
    print("2. Gastarle a tu profe favorita (10000)")
    print("3. Ganar dinero (acumulativo) (5000)")
    
    opcion = int(input("Ingresa el número de tu opción: "))
    
    if opcion == 1:
        gasto_total += 6000
        presupuesto -= 6000
        print("Has pagado 6000 por transporte")
    elif opcion == 2:
        gasto_total += 10000
        presupuesto -= 10000
        print("Has gastado 10000 en tu profe favorita")
    elif opcion == 3:
        acumulado += 5000
        print("Has ganado 5000")
    
    print("Tu presupuesto actual es de", presupuesto)
    print("Tu acumulado actual es de", acumulado)
    
    respuesta = input("¿Quieres repetir las opciones? (si/no): ")
    if respuesta.lower() == "no":
        repetir = False
   
print("Has gastado un total de", gasto_total, "en las opciones.")


