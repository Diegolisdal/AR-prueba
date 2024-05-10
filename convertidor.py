import cv2
import numpy as np
import ARToolKitPlus as ar

# Cargar la imagen
image = cv2.imread('pinball.jpg', cv2.IMREAD_GRAYSCALE)

# Inicializar un detector de características
detector = ar.SimplePatternDetector()

# Crear un patrón ARToolKit
pattern = ar.Pattern(image.shape[1], image.shape[0])
pattern.setImage(image)

# Guardar el patrón en un archivo .patt
pattern.saveToFile('patron.patt')
