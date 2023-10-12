
import numpy as np #Para trabajar con arreglos (matrices)
import matplotlib.pyplot as plt  #Para ver la imagen


def convolucion (img, kernel):
    img_arr = np.array(img, dtype=np.float32)

    filas_img, cols_img = img.shape #Guardo las filas y columnas de la imagen
    filas_kernel, cols_kernel = kernel.shape #Guardo las filas y columnas del kernel
    conv_img = np.zeros(shape=(filas_img, cols_img)) #Creo un arreglo para la imagen modificada por el kernel

    padding_fila = filas_kernel // 2
    padding_col = cols_kernel // 2
    img_pad = np.pad(img_arr, padding_fila, mode='edge') #Relleno los bordes de la imagen con los valores vecinos

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
            # aplica normalizacion a cada pixel de la imagenn
    min_values = np.min(conv_img)
    max_values = np.max(conv_img)
    conv_img = (conv_img - min_values) / (max_values - min_values)

    return conv_img

def convolucion_rgb (img, kernel):
    img_arr = np.array(img, dtype=np.float32)

    filas_img, cols_img, canales = img_arr.shape 
    filas_kernel, cols_kernel = kernel.shape 
    conv_img = np.zeros(shape=(filas_img, cols_img, canales)) 

    padding_fila = filas_kernel // 2
    padding_col = cols_kernel // 2
    img_pad = np.pad(img_arr, ((padding_fila, padding_fila), (padding_col, padding_col), (0, 0)), mode='edge') 
    
    for fila_img in range(filas_img):
        for col_img in range(cols_img):
            for canal in range(canales): #itera a traves de los canales de la imagen
                resultado = 0
                for fila_kernel in range(filas_kernel):
                    for col_kernel in range(cols_kernel):
                        fila_actual = fila_img - padding_fila + fila_kernel
                        col_actual = col_img - padding_col + col_kernel
                        resultado += img_pad[fila_actual, col_actual, canal] * kernel[fila_kernel, col_kernel]
                conv_img[fila_img, col_img, canal] = resultado
        # aplica normalizacion a cada pixel de la imagenn
    min_values = np.min(conv_img, axis=(0, 1)) # con axis te devuelve el valor max y min de cada canal
    max_values = np.max(conv_img, axis=(0, 1))
    conv_img = (conv_img - min_values) / (max_values - min_values)
    return conv_img



