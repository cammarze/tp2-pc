import numpy as np

# Funciones para realizarla conovlcuion en escala de grises y RGB, dado una imagen de entrada se realiza
#la convolucion con un kernel especificado. Al finalizar, se lleva a cabo el relleno de bordes
#normalización y ajuste de tipos de datos.

def convolucion (img, kernel):
    """
    Realiza una convolución en escala de grises.
    Parameters:
    img -- La imagen de entrada (escala de grises).
    kernel (np.array) -- El kernel de convolución en formato NumPy array.

    Returns:
    np.array -- La imagen resultante después de la convolución.
    """
    img_arr = np.array(img, dtype=np.float32)

    filas_img, cols_img = img.shape #Guardo las filas y columnas de la imagen
    filas_kernel, cols_kernel = kernel.shape #Guardo las filas y columnas del kernel
    conv_img = np.zeros(shape=(filas_img, cols_img)) #Creo un arreglo para la imagen modificada por el kernel

    padding_fila = filas_kernel // 2
    padding_col = cols_kernel // 2
    img_pad = np.pad(img_arr, ((padding_fila, padding_fila), (padding_col, padding_col)), mode='edge') #Relleno los bordes de la imagen con los valores vecinos

    for fila_img in range(filas_img):
        for col_img in range(cols_img):#itera a traves de as filas y columnas de la imagen
            #multiplica una parte de la imagen por el kernel
            conv_img[fila_img, col_img] = np.sum(img_pad[fila_img:fila_img+filas_kernel, col_img:col_img+cols_kernel] * kernel)
            # con np.sum calcula la suma de los elementos

    min_values = np.min(conv_img)
    max_values = np.max(conv_img)
    conv_img = (conv_img - min_values) / (max_values - min_values) #Pixeles quedan entre 0 y 1
    conv_img *= 255
    conv_img = conv_img.astype(np.uint8) #Convierte

    return conv_img
    
def convolucion_rgb (img, kernel):
    """
    Realiza una convolución en una imagen RGB.

    Parameters:
    img -- La imagen de entrada con tres canales (rojo, verde y azul).
    kernel (np.array) -- El kernel de convolución en formato NumPy array.

    Returns:
    np.array -- La imagen resultante después de la convolución.
    """
    img_arr = np.array(img, dtype=np.float32)

    filas_img, cols_img, canales = img_arr.shape 
    filas_kernel, cols_kernel = kernel.shape 
    conv_img = np.zeros(shape=(filas_img, cols_img, canales)) 

    padding_fila = filas_kernel // 2
    padding_col = cols_kernel // 2
    img_pad = np.pad(img_arr, ((padding_fila, padding_fila), (padding_col, padding_col), (0, 0)), mode='edge') 

    for canal in range(canales):
        for fila_img in range(filas_img):
            for col_img in range(cols_img):
                conv_img[fila_img, col_img, canal] = np.sum(img_pad[fila_img:fila_img+filas_kernel, col_img:col_img+cols_kernel, canal] * kernel)
        # aplica normalizacion a cada pixel de la imagenn
    min_values = np.min(conv_img, axis=(0, 1)) # con axis te devuelve el valor max y min de cada canal
    max_values = np.max(conv_img, axis=(0, 1))
    conv_img = (conv_img - min_values) / (max_values - min_values) #Pixeles quedan entre 0 y 1
    conv_img *= 255
    conv_img = conv_img.astype(np.uint8) #Convierte los pixeles con valores float a int (trunca)
    return conv_img

#Umbralizacion
def umbralizacion(img_arr:list) -> list:
    umbral = input('Ingrese umbral: ')
    while not umbral.isdecimal() or not 0 <= float(umbral) <= 255: 
        umbral = input('Error. Ingrese un numero entre 0 y 255: ')
    umbral = float(umbral)

    img_arr[img_arr >= umbral] = 255
    img_arr[img_arr < umbral] = 0
    return img_arr


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
    """
    Crea un kernel personalizado a partir de los datos ingresados por el ususario.
    La funcion le solicita al usuario que ingrese el tamaño del kernel a realizar (debe ser un numero entero e impar). Luego, 
    pide los valores para cada fila del kernel. Estos son almacenados en un formato Numpy array. 

    Returns:
    np.array -- Kernel personalizado creado por el usuario
    """
    n = input('Ingrese el tamaño del kernel: ')
    while not n.isdecimal() or int(n) % 2 == 0: #error en caso de que el usuario ingresa un str o el tamaño del kernel es par
        n = input('Ingrese el tamaño del kernel (debe ser un numero impar): ')
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
