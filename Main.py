import sqlite3
import math
import sys
import time
import random
import string
import re
import difflib
import Calculadora
import EstrellaDeDiamantes
import difflib
import config
import Vocabulario

# Establish database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create user table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')

# Function to validate email format
def validate_email(email):
    pattern = re.compile(r'^[\w\.-]+@[a-zA-Z\d]+\.[a-zA-Z]{2,}$')
    return pattern.match(email)

# Function to register a new user
def sign_up(username, email, password):
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    print("Usuario registrado exitosamente.")

# Function to log in
def login(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result:
        stored_password = result[0]
        if difflib.SequenceMatcher(None, password, stored_password).ratio() >= 0.79:
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("La contraseña es incorrecta.")
    else:
        print("El usuario no existe.")
    return False

# Function to log out
def logout():
    print("Sesión cerrada exitosamente.")

# Function to recover password
def forgot_password(username):
    # Implementation for password recovery
    pass

# Function to recover username
def forgot_username(password):
    # Implementation for username recovery
    pass

# Main function
def main():
    session_active = False

    while True:
        print("\n¿Qué desea hacer?")
        if session_active:
            print("1. Cerrar sesión")
        else:
            print("1. Iniciar sesión")
            print("2. Registrarse")
        print("3. Olvidé Usuario")
        print("4. Olvidé Contraseña")
        if session_active:
            print("5. Calculadora")
            print("6. Estrella de diamantes")
            print("7. Herramientas de vocabulario")
        print("8. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            if session_active:
                logout()
                session_active = False
            else:
                username = input("Ingrese su nombre de usuario: ")
                password = input("Ingrese su contraseña: ")
                if login(username, password):
                    session_active = True
        elif opcion == '2' and not session_active:
            username = input("Elige un nombre de usuario: ")
            email = input("Ingresa tu correo electrónico: ")
            while not validate_email(email):
                print("El formato de correo electrónico es incorrecto.")
                email = input("Ingresa tu correo electrónico: ")
            password = input("Elige una contraseña: ")
            sign_up(username, email, password)
        elif opcion == '3':
            password = input("Ingrese su contraseña: ")
            forgot_username(password)
        elif opcion == '4':
            username = input("Ingrese su nombre de usuario: ")
            forgot_password(username)
        elif opcion == '5' and session_active:
            Calculadora.calcmenu()  # Call calcmenu function from Calculadora module
        elif opcion == '6' and session_active:
            EstrellaDeDiamantes.estrella(int(input("Longitud de la estrella (lo recomendado es de 4 a 20): ")))  # Call estrella function from EstrellaDeDiamantes module
        elif opcion == '7' and session_active:
            Vocabulario.vocabmenu()  # Call vocabmenu function from Vocabulario module
        elif opcion == '8':
            print("¡Hasta luego!")
            sys.exit()
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()

# Close database connection
conn.close()
