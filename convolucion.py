from PIL import Image #Para leer imagenes
import numpy as np #Para trabajar con arreglos (matrices)
import matplotlib.pyplot as plt  #Para ver la imagen

#Pone el kernel que quieras
kernel = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]) 

img_ing = input('Ingrese el nombre del archivo de la imagen: ')
imagen = Image.open('test_images/' + img_ing)
img_arr = np.array(imagen)

filas_img, cols_img = img_arr.shape #Guardo las filas y columnas de la imagen
filas_kernel, cols_kernel = kernel.shape #Guardo las filas y columnas del kernel
conv_img = np.zeros(shape=(filas_img, cols_img)) #Creo un arreglo para la imagen modificada por el kernel

padding_fila = filas_kernel // 2
padding_col = cols_kernel // 2

for fila_img in range(padding_fila, filas_img - padding_fila): #Evito los bordes de la imagen
    for col_img in range(padding_col, cols_img - padding_col):
        resultado = 0
        for fila_kernel in range(filas_kernel):
            for col_kernel in range(cols_kernel):
                #Me muevo segun la posicion en el kernel
                fila_actual = fila_img - padding_fila + fila_kernel
                col_actual = col_img - padding_col + col_kernel
                resultado += img_arr[fila_actual, col_actual] * kernel[fila_kernel, col_kernel]
        conv_img[fila_img, col_img] = resultado

plt.imshow(conv_img, cmap='gray')
plt.show()