import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)

rastreador = HandDetector(detection=0.8, maxHands=2)
while True:

    # exito => lee la imagen
    # imagen => guarda la imagen que esta capturando la webcam
    exito, imagen = webcam.read()

    coordenadas, imagen_manos = rastreador.findHands(imagen)
    cv2.imshow("Proyecto 4 - IA", imagen)

    # el metodo waitkey espera alguna tecla
    if cv2.waitKey(1) != -1:
        break

# Esto que nos libere la imagen de la captura
webcam.release()
# Libera todas las camaras
cv2.destroyAllWindows()
