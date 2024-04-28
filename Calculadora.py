import math
import sys
import time
import random
import string
import re
import difflib
from config import DelayTimeVar

def CambiarDelayVar():
    new_delay = int(input("Ingrese nuevo valor de espera: "))
    # Update the imported DelayTimeVar with the new value
    DelayTimeVar = new_delay
    return DelayTimeVar

def sumar():
    numero1suma = obtener_numero("Primer número")
    numero2suma = obtener_numero("Segundo número")
    resultado = numero1suma + numero2suma
    sys.stdout.write("El resultado es: ")
    print(resultado)
    time.sleep(DelayTimeVar)

# Función para calcular la resta de dos números
def restar():
    numero1resta = obtener_numero("Primer número")
    numero2resta = obtener_numero("Segundo número")
    resultado = numero1resta - numero2resta
    sys.stdout.write("El resultado es: ")
    print(resultado)
    time.sleep(DelayTimeVar)

# Función para calcular la multiplicación de dos números
def multiplicar():
    numero1multiplicar = obtener_numero("Primer número")
    numero2multiplicar = obtener_numero("Segundo número")
    resultado = numero1multiplicar * numero2multiplicar
    sys.stdout.write("El resultado es: ")
    print(resultado)
    time.sleep(DelayTimeVar)

# Función para calcular la división de dos números
def dividir():
    numero1dividir = obtener_numero("Primer número")
    numero2dividir = obtener_numero("Segundo número")
    if numero2dividir == 0:
        print("No se puede dividir por cero.")
        return
    resultado = numero1dividir / numero2dividir
    sys.stdout.write("El resultado es: ")
    print(resultado)
    time.sleep(DelayTimeVar)

# Función para calcular la raíz cuadrada de un número
def raizcuadrada():
    raiz = obtener_numero("Número para sacarle la raíz cuadrada")
    if raiz < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
        return
    raizresultado = math.sqrt(raiz)
    sys.stdout.write("El resultado es: ")
    print(raizresultado)
    time.sleep(DelayTimeVar)

# Función para calcular la longitud de una circunferencia
def circunferencia():
    radio = obtener_numero("Radio de la circunferencia")
    if radio < 0:
        print("El radio no puede ser negativo.")
        return
    pi = math.pi
    longitud = 2 * pi * radio
    print("Longitud de la circunferencia:", longitud)
    time.sleep(DelayTimeVar)

# Función para calcular la potencia de un número
def elevar():
    numero1elevar = obtener_numero("Base")
    numero2elevar = obtener_numero("Exponente")
    resultado = math.pow(numero1elevar, numero2elevar)
    sys.stdout.write("El resultado es: ")
    print(resultado)
    time.sleep(DelayTimeVar)

# Función para calcular el coseno de un número
def coseno():
    cost = obtener_numero("Número para sacarle el coseno")
    cosresultado = math.cos(cost)
    sys.stdout.write("El resultado es: ")
    print(cosresultado)
    time.sleep(DelayTimeVar)

# Función para convertir de radianes a grados
def radianes():
    rads = obtener_numero("Número para convertir de radianes a grados")
    radresultado = math.degrees(rads)
    sys.stdout.write("El resultado es: ")
    print(radresultado)

# Función para convertir de grados a radianes
def grados():
    grads = obtener_numero("Número para convertir de grados a radianes")
    gradres = math.radians(grads)
    sys.stdout.write("El resultado es: ")
    print(gradres)

# Función para mostrar el valor de pi
def npi():
    print("El valor de pi es:", math.pi)
    time.sleep(DelayTimeVar)

# Función para mostrar el valor de e
def enum():
    print("El valor de e es:", math.e)
    time.sleep(DelayTimeVar)

# Función para calcular el número Fibonacci de un número
def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

# Función para mostrar el número Fibonacci de un número
def fib_menu():
    fibnum = int(input("Número Fibonacci: "))
    print("El resultado es:", fib(fibnum))
    time.sleep(DelayTimeVar)

# Función para obtener un número
def obtener_numero(mensaje):
    while True:
        valor = input(mensaje + ": ")
        if not valor.replace(".", "", 1).isdigit():
            print("Valor no válido. Ingrese el valor nuevamente.")
        else:
            return float(valor)


def calcmenu():
    while True:
        print("\n¿Qué operación desea realizar?")
        print("0. Cambiar tiempo de espera")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Raíz Cuadrada")
        print("6. Longitud de la Circunferencia")
        print("7. Elevar a la Potencia")
        print("8. Coseno")
        print("9. Convertir a Radianes")
        print("10. Convertir a Grados")
        print("11. Mostrar el valor de Pi")
        print("12. Mostrar el valor de e")
        print("13. Calcular el número Fibonacci")
        print("14. Volver al menú anterior")
        operation = input("Ingrese su opción: ")
        if operation == '0':\
            CambiarDelayVar()
        elif operation == '1':
            sumar()
        elif operation == '2':
            restar()
        elif operation == '3':
            multiplicar()
        elif operation == '4':
            dividir()
        elif operation == '5':
            raizcuadrada()
        elif operation == '6':
            circunferencia()
        elif operation == '7':
            elevar()
        elif operation == '8':
            coseno()
        elif operation == '9':
            radianes()
        elif operation == '10':
            grados()
        elif operation == '11':
            npi()
        elif operation == '12':
            enum()
        elif operation == '13':
            fib_menu()
        elif operation == '14':
            break
        else:
            print("Opción inválida. Intente nuevamente.")