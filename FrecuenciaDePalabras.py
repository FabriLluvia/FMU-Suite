import time
from config import DelayTimeVar

def frecuencia_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def frecuencia_palabras_menu():
    text = input("Introduce un texto para contar la frecuencia de palabras: ")
    resultado = frecuencia_palabras(text)
    print(resultado)
    time.sleep(DelayTimeVar)

if __name__ == "__main__":
    frecuencia_palabras_menu()
