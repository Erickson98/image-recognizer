
import cv2
import pytesseract
from PIL import Image, ImageFilter
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# Cargar la imagen
imagen = cv2.imread('imagen_aumentada2.png')

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
