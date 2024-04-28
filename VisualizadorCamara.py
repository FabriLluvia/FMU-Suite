import cv2

# Función para capturar video desde la cámara
def visualizar_camara():
    # Inicializar el objeto VideoCapture para capturar video desde la cámara
    captura = cv2.VideoCapture(0)

    # Verificar si la cámara se ha abierto correctamente
    if not captura.isOpened():
        print("No se pudo abrir la cámara")
        return

    # Bucle para capturar y mostrar video de la cámara
    while True:
        # Capturar un fotograma desde la cámara
        ret, frame = captura.read()

        # Verificar si el fotograma se ha capturado correctamente
        if not ret:
            print("No se pudo capturar el fotograma")
            break

        # Mostrar el fotograma en una ventana
        cv2.imshow('Visualizador de camara', frame)

        # Esperar 1 milisegundo y verificar si se presiona la tecla 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar el objeto VideoCapture y cerrar todas las ventanas
    captura.release()
    cv2.destroyAllWindows()

# Llamar a la función para visualizar la cámara
visualizar_camara()
