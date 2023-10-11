from PIL import Image #Para leer imagenes
import numpy as np #Para trabajar con arreglos (matrices)
import matplotlib.pyplot as plt  #Para ver la imagen
import funciones as f

img_ing = input('Ingrese el nombre del archivo de la imagen: ')
imagen = Image.open('test_images/' + img_ing)
img_arr = np.array(imagen)

print(img_arr.shape)
plt.imshow(img_arr, cmap='gray')
plt.show()

for i, operacion in enumerate(f.operaciones.values()):
    print(f'{i}. {operacion}')
kernel = f.operaciones[input('Ingrese la operacion: ')]()

filas_img, cols_img = img_arr.shape #Guardo las filas y columnas de la imagen
filas_kernel, cols_kernel = kernel.shape #Guardo las filas y columnas del kernel
conv_img = np.zeros((filas_img, cols_img)) #Creo un arreglo para la imagen modificada por el kernel

padding_fila = filas_kernel // 2
padding_col = cols_kernel // 2
img_pad = np.pad(img_arr, ((padding_fila, padding_fila), (padding_col, padding_col)), mode='edge') #Relleno los bordes de la imagen con los valores vecinos

for fila_img in range(filas_img): #Evito los bordes de la imagen
    for col_img in range(cols_img):
        resultado = 0
        for fila_kernel in range(filas_kernel):
            for col_kernel in range(cols_kernel):
                #Me muevo en la imagen con padding
                fila_actual = fila_img - padding_fila + fila_kernel
                col_actual = col_img - padding_col + col_kernel
                resultado += img_pad[fila_actual, col_actual] * kernel[fila_kernel, col_kernel]
        conv_img[fila_img, col_img] = resultado

print(conv_img.shape)
plt.imshow(conv_img, cmap='gray')
plt.show()