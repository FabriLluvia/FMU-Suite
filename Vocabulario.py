import FrecuenciaDePalabras
def vocabmenu():
    while True:  # 'True' should be capitalized
        print("\n¿Qué desea realizar?")
        print("1. Contar la frecuencia de palabras de un texto")
        print("2. Contar cuantas palabras tiene un texto")
        print("3. Volver al menú anterior")
        opcion = input("Ingrese su opción: ")
        if opcion == '1':
            frecuencia_de_palabras_menu()
        elif opcion == '2':
            contar_palabras_menu()
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# You need to define frecuencia_de_palabras_menu() for option 1 functionality
def frecuencia_de_palabras_menu():
    text = input("Introduce un texto para contar la frecuencia de palabras: ")
    print(FrecuenciaDePalabras.frecuencia_palabras(text))

