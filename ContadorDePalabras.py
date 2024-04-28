import time
from config import DelayTimeVar

def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

def contar_palabras_menu():
    text = input("Introduce un texto para contar la cantidad de palabras: ")
    resultado = contar_palabras()
    print("El texto tiene", resultado, "palabras.")
    time.sleep(DelayTimeVar)
