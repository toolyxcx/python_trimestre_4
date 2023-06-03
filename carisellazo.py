import random

def lanzarMoneda():
    jugador = input("Ingrese su nombre: ")
    resultado = random.choice(["cara", "sello"])
    print(f"{jugador} lanzó la moneda y salió {resultado}")
    return resultado

def jugar(saldo_inicial):
    eleccion = input("Elige cara o sello: ")
    apostar = input("¿Deseas apostar? (si/no): ")
    if apostar.lower() == "no":
        resultado = lanzarMoneda()
        if resultado == eleccion:
            print("¡Ganaste!")
            ganar(0, saldo_inicial)
        else:
            print("Perdiste.")
            perder(0, saldo_inicial)
    elif apostar.lower() == "si":
        monto = int(input("¿Cuánto deseas apostar?: "))
        if monto > saldo_inicial:
            print("No tienes suficiente saldo para realizar esa apuesta.")
            jugar(saldo_inicial)
            return
        resultado = lanzarMoneda()
        if resultado == eleccion:
            print("¡Ganaste!")
            ganar(monto, saldo_inicial)
        else:
            print("Perdiste.")
            perder(monto, saldo_inicial)
    else:
        print("Opción inválida. Intenta de nuevo.")
        jugar(saldo_inicial)

def ganar(apostado, saldo_inicial):
    ganancia = apostado * 2
    saldo_actual = saldo_inicial + ganancia
    print(f"Ganaste {ganancia} pesos.")
    print(f"Saldo actual: {saldo_actual} pesos")

def perder(apostado, saldo_inicial):
    saldo_actual = saldo_inicial - apostado
    print(f"Perdiste {apostado} pesos.")
    print(f"Saldo actual: {saldo_actual} pesos")

saldo_inicial = int(input("Ingrese su saldo inicial: "))
jugar(saldo_inicial)
