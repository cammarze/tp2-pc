import numpy as np

#Umbralizacion
def umbralizacion(img_arr:list) -> list:
    umbral = input('Ingrese umbral: ')
    while not umbral.isdecimal() or not 0 <= float(umbral) <= 255:
        umbral = input('Error. Ingrese un numero entre 0 y 255: ')
    umbral = float(umbral)

    img_arr[img_arr >= umbral] = 255
    img_arr[img_arr < umbral] = 0
    return img_arr

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
