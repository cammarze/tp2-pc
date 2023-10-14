import numpy as np
import matplotlib.pyplot as plt

#Umbralizacion
def umbralizacion(img_arr:list) -> list:
    umbral = input('Ingrese umbral: ')
    while not umbral.isdecimal() or not 0 <= float(umbral) <= 255:
        umbral = input('Error. Ingrese un numero entre 0 y 255: ')
    umbral = float(umbral)

    img_arr[img_arr >= umbral] = 255
    img_arr[img_arr < umbral] = 0
    return img_arr

#Convolucion blanco y negro
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
    conv_img = (conv_img - min_values) / (max_values - min_values) #Pixeles quedan entre 0 y 1
    conv_img *= 255
    conv_img = conv_img.astype(np.uint8) #Convierte los pixeles con valores float a int (trunca)

    return conv_img

#Convolucion color
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
    conv_img = (conv_img - min_values) / (max_values - min_values) #Pixeles quedan entre 0 y 1
    conv_img *= 255
    conv_img = conv_img.astype(np.uint8) #Convierte los pixeles con valores float a int (trunca)
    return conv_img

#Normalizacion
def normalizacion (salida):
    valor_minimo = np.min(salida)
    valor_maximo = np.max(salida)
    normalizado = ((salida - valor_minimo) / (valor_maximo - valor_minimo) * 255)
    return normalizado

#Kernels
def identidad ():
    kernel_id = np.array([[0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0]])
    return kernel_id

def negativo():
    kernel_neg = np.array([[0, 0, 0],
                          [0, -1, 0],
                          [0, 0, 0]])
    return kernel_neg

def sobel_vertical ():
    kernel_sovelver = np.array([[-1, -2, -1],
                            [0, 0, 0],
                            [1, 2, 1]]) 
    return kernel_sovelver

def sobel_horizontal ():
    kernel_soberlhor = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])
    return kernel_soberlhor

def sharpen ():
    kernel_sharpen = np.array([[-1, -1, -1],
                               [-1, 8, -1],
                               [-1, -1, -1]])
    return kernel_sharpen

def gaussian ():
    kernel_gaussian = np.array([[1, 4, 6, 4, 1],
                               [4, 16, 24, 16, 4],
                               [6, 24, 36, 24, 6],
                               [4, 16, 24, 16, 4],
                               [1, 4, 6, 4, 1]])
    return kernel_gaussian

def unsharpen ():
    kernel_unsharpen = -1 * gaussian()

    return kernel_unsharpen

def box_blur ():
    kernel_boxblur = np.ones((11,11), dtype = int)
    return kernel_boxblur

def lens_blur():
    kernel_lensblur = np.array([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
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
    return kernel_lensblur

def motion_blur():
    kernel_motionblur = np.eye(11, dtype = int)[:, ::-1]
    return kernel_motionblur

def kernel_personalizado ():
    n = input('Ingrese un numero: ')
    while not n.isdecimal():
        n = input('Error. Ingrese un numero: ')
    n = int(n)

    personalizado_array = np.empty((n,n), dtype = float)
    for f in range(1, n + 1):
        while True: 
            fila = (input(f"Ingrese los valores de la fila {f} separados por espacios: ")) 
            if len(fila.split()) != n:
                print(f'ERROR: Debe ingresar exactamente {n} numeros')
            else:       
                try:
                    elementos_lista = [float(x) for x in fila.split()]
                    personalizado_array [f -1] = elementos_lista
                    break
                except ValueError:
                    print('ERROR, los valores no son numeros reales')
    return personalizado_array

#Diccionario de operaciones
operaciones = {'1':umbralizacion, '2':identidad, '3':negativo, '4':sobel_vertical, '5':sobel_horizontal,
               '6':sharpen, '7':gaussian, '8':unsharpen, '9':box_blur, '10':lens_blur,
               '11':motion_blur, '12':kernel_personalizado}
