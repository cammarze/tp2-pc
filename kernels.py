import numpy as np

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

def kernel_personalizado (n):
    personalizado_array = np.empty((n,n), dtype = float)

    for f in range(1, n + 1):
        fila =  (input(f"Ingrese los valores de la fila {f} separados por espacios:"))            
        elementos_lista = [float(x) for x in fila.split()]
        personalizado_array [f -1] = elementos_lista
            
    return personalizado_array

try:
    print(kernel_personalizado(int(input("Ingrese el tamaño del kernel: "))))

except ValueError:
    print('ERROR, los valores no son numeros reales')
