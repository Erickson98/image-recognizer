
import pytesseract
from PIL import Image, ImageFilter
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# Ruta de la imagen original
imagen_ruta = 'img2.png'

# Cargar la imagen original
imagen_original = Image.open(imagen_ruta)

# Definir el factor de escala para aumentar la resolución
factor_escala = 4  # Por ejemplo, duplicar la resolución

# Calcular las nuevas dimensiones de la imagen
nuevo_ancho = imagen_original.width * factor_escala
nuevo_alto = imagen_original.height * factor_escala

# Aplicar la interpolación para aumentar la resolución
imagen_aumentada = imagen_original.resize(
    (nuevo_ancho, nuevo_alto), Image.LANCZOS)

# Guardar la imagen aumentada en un nuevo archivo
imagen_aumentada.save('imagen_aumentada3.png')

# Ruta de la imagen a capturar
imagen_ruta = 'imagen_aumentada3.png'
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
