#Wenas. Este es el codigo :). Hay 2 cosas que no hice porque me parece que seria mejor hacerlas
#una vez que tengamos el codigo del TP completo. Una es el manejo de excepciones (si el usuario ingresa el nombre de
#una imagen que no existe o si ingresa un numero para el umbral que no es valido, por ej). La otra es la definicion
#de funciones (una funcion para mostrar la imagen, por ej). Me pareceria una buena idea que definamos todas las
#funciones que usemos para el TP en un archivo separado para que sea mas facil la lectura del codigo

from PIL import Image #Para leer imagenes
import numpy as np #Para trabajar con arreglos (matrices)
import matplotlib.pyplot as plt  # Para ver la imagen

img_ing = input('Ingrese el nombre del archivo de la imagen: ')
imagen = Image.open('test_images/' + img_ing)
img_arr = np.array(imagen)

#Mostrar la imagen en una ventana aparte
if len(img_arr.shape) > 2:
    plt.imshow(img_arr)
    plt.show()
else:
    plt.imshow(img_arr, cmap='gray')
    plt.show()

umbral = float(input('Ingrese umbral: '))
img_arr[img_arr >= umbral] = 255
img_arr[img_arr < umbral] = 0

#Mostrar la imagen en una ventana aparte
if len(img_arr.shape) > 2:
    plt.imshow(img_arr)
    plt.show()
else:
    plt.imshow(img_arr, cmap='gray')
    plt.show()