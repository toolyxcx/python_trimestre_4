#1. Declaración de un método sin parámetros
def sumar(n1, n2):
    sumar=n1+n2
    print(f"La suma entre {n1} y {n2} es {sumar}")

#2. Declaración método con parámetros
def restar(n1,n2):
    #Cuerpo método
    restar=n1-n2
    print(f"La resta entre {n1} y {n2} es {restar} ")

#3. Declaración método con valor de retorno
def multiplicar(n1,n2):
    multiplicar=n1*n2
    print(f"La Multiplicación entre {n1} y {n2} es {multiplicar} ")

def division(n1, n2):
    division= n1/n2
    print(f"La division entre {n1} y {n2} es {division} ")


def sumarm(n1, n2):
    sumarm=n1+n2
    promedio=sumarm/2
    print(f"la suma entre {n1} y {n2} es {sumarm} y el promedio es {promedio}")

def sumarp():
    seguir=="si"
    suma=0
    while seguir=="si":
        numero=int(input("Digite un numero entero"))
        suma=suma+numero
        seguir=input("para seguir ingrese si de lo contrario no")
        return suma

print("Menu opciones")

num1=int(input("Ingrese el número 1 "))
num2=int(input("Ingrese el número 2 "))

op=int(input("Ingrese la opción segun la operación a realizar \n 1.Suma 2.Resta 3.Multiplicación 4.División 5.Promedio \n"))

if op==1:
    sumar(num1, num2)

elif op==2:
    restar(num1,num2)

elif op==3:
    multiplicar(num1, num2)

elif op==4:
    division(num1,num2)
elif op==5:
    sumarm(num1,num2)    
else:
    print("invalid")