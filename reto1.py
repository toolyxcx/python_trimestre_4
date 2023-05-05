tipogasolina = input("Ingrese el tipo de gasolina que desea (corriente o diesel): ")

if tipogasolina.lower() == "corriente":
    preciogasolina = 10800
elif tipogasolina.lower() == "diesel":
    preciogasolina = 9800
else:
    print("Tipo de gasolina no válido. Por favor ingrese 'corriente' o 'diesel'.")
    exit()

valor = float(input("Ingrese el valor a tanquear para el vehículo: "))
galones = valor / preciogasolina
print("Usted tanqueó", galones, "galones de gasolina", tipogasolina.lower() + ".")

