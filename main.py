
import cv2
import pytesseract
import keyboard
import time
import mouse
from PIL import Image, ImageFilter, ImageGrab


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# Cargar la imagen
imagen = cv2.imread('screenshot_windows_shift_s.png')

# Aplicar un filtro de enfoque
imagen_enfocada = cv2.GaussianBlur(imagen, (0, 0), 3)
imagen_nitida = cv2.addWeighted(imagen, 1.5, imagen_enfocada, -0.5, 0)

cv2.imwrite('imagen_aumentada36.png', imagen_nitida)


# Ruta de la imagen a capturar
imagen_ruta = 'imagen_aumentada36.png'
print(imagen_ruta)
# Capturar la imagen
imagen = Image.open(imagen_ruta)
imagen_nitida = imagen.filter(ImageFilter.SHARPEN)
imagen_filtrada = imagen_nitida.filter(ImageFilter.MaxFilter)
# Extraer el texto de la imagen utilizando pytesseract
texto = pytesseract.image_to_string(
    imagen, lang='eng', config='--psm 6 --oem 3')

# Imprimir el texto extraído

print(texto)


def on_s_release():
    # Capturar la región seleccionada por "Windows + Shift + S"
    screenshot = ImageGrab.grabclipboard()

    # Guardar la screenshot en un Aarchivo
    if screenshot:
        screenshot.save("screenshot_windows_shift_s.png")
        print("Screenshot guardada como screenshot_windows_shift_s.png")
        return True

    # Detener la detección del evento después de capturar la screenshot
    return False


def capture_proccess():
    keyboard.press_and_release("win+shift+s")


def screenShootCheck():
    capture_image_check = False
    while capture_image_check:
        print("Estoy en false yet")
        time.sleep(1)
        if on_s_release():
            capture_image_check = True


def capture_screenshot_windows_shift_s():
    # Mantener el programa en ejecución hasta que la tecla "s" sea presionada y suelta

    while True:
        keyboard.add_hotkey('left windows+shift+f', capture_proccess)
        keyboard.wait('left windows+shift+f')

        mouse.wait('left', 'up')
        time.sleep(0.5)  # 1-1
        if not on_s_release():  # 2-1
            screenShootCheck()

        time.sleep(1)

# Capturar la screenshot


capture_screenshot_windows_shift_s()
