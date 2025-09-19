#Parte5
#Capturar video en tiempo real y detectar bordes con el operador de Canny en cada cuadro
import cv2
import numpy as np

# Inicializar la captura de video
cap = cv2.VideoCapture(0)

while True:
    # Leer un cuadro del video
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar el operador de Canny
    edges = cv2.Canny(gray, 100, 200)

    # Mostrar el cuadro original y el resultado
    cv2.imshow('Cuadro Original', frame)
    cv2.imshow('Detección de Bordes', edges)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()