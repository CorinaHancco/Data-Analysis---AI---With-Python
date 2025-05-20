import pyautogui
import pyperclip
import webbrowser # para abrir el navegador
import time
import yfinance

ticker = input("Digita el codigo de la acción: ")
data = yfinance.Ticker(ticker).history("6mo")
cierre = data.Close

maximo = round(cierre.max(),2)
minimo = round(cierre.min(),2)
medio = round(cierre.mean(),2)

# Abrir mi correo electronico en el navegador
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

time.sleep(3)

pyautogui.PAUSE = 3 # Que espere 3 segundos entre cada uno de los comandos a ejecutar

pyautogui.click(173,238) # click en esta coordenada x=173, y=238 calculada con pyautogui.position()


destinatario = "hanccovargascorina@gmail.com"
asunto = "Análisis acciones de los últimos 6 meses"
mensaje = f"""
Hola CORI 😉,
Realizo el envio del análisis de las acciones de los ultimo 6 meses de {ticker}:

Cotización máxima: USD {maximo}
Cotización mínima: USD {minimo}
Valor medio: USD {medio}

"""

# Copiar el destinatario en portapapeles
pyperclip.copy(destinatario)

# Copiar lo que hay en porta papeles a donde esta el mouse
pyautogui.hotkey("ctrl","v")  # hotkey ejecuta comandos de mi teclado automaticamente
pyautogui.hotkey("tab")

pyperclip.copy(asunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy(mensaje)
pyautogui.hotkey("ctrl","v")


# Enviamos el correo
pyautogui.click(1198,969) # x=1198, y=969 Posicion del boton enviar

# Cerramos la ventana del navegar abierto
pyautogui.hotkey("ctrl","f4")

