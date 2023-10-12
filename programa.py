from PIL import Image #Para leer imagenes
import numpy as np #Para trabajar con arreglos (matrices)
import matplotlib.pyplot as plt  #Para ver la imagen
import funciones as f
import convolucion as conv

def open_image (): #funcion para abrir la imagen
    try:
        img_ing = input('Ingrese el nombre del archivo de la imagen: ')
        imagen = Image.open(img_ing)
            # imagen = Image.open('test_images//' + img_ing)
        img_arr = np.array(imagen)
        return img_arr

    except FileNotFoundError:
        print("Imagen no encontrada!")
        exit()
    
if __name__ == "__main__":
    img_arr = np.array(open_image())
    plt.imshow(img_arr, cmap='gray')
    plt.show()

    print('OPERACIONES')
    print('-----------')
    for i, operacion in enumerate(f.operaciones.values(), 1): 
        print(f'{i}. {operacion.__name__}') #imprimir los tipos de kernel

    opcion = input('Ingrese la operacion: ') #si la opcion ingresada esta fuera del rango de opciones, muestra mensaje de error
    if 1 > int(opcion) or int(opcion) > 12:
        print("Operación inválida!")
        exit()

    if opcion == '1': 
        img_arr = f.umbralizacion(img_arr) 

    else:
        kernel = f.operaciones[opcion]()

        if len(img_arr.shape) == 2:  #verifica si la imagen es en escala de grises (2D)

            convolucion_img = conv.convolucion(img_arr, kernel)
            plt.imshow(convolucion_img, cmap ='gray')
            plt.show()

        else: # para las imagenes RGB
            img_conv_rgb = conv.convolucion_rgb(img_arr, kernel)
            plt.imshow(img_conv_rgb, cmap = 'gray')
            plt.show()
        
    print('Operacion realizada con exito!')

