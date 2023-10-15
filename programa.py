from PIL import Image #Para leer imagenes
import numpy as np #Para trabajar con arreglos (matrices)
import matplotlib.pyplot as plt  #Para mostrar la imagen
import funciones as f

def main():

    try:
        img_ing = input('Ingrese el nombre del archivo de la imagen: ')
        img = Image.open('test_images//' + img_ing)
        img_arr = np.array(img)
        
        plt.imshow(img_arr, cmap='gray')
        plt.show()

        print('OPERACIONES')
        print('-----------')
        for i, operacion in enumerate(f.operaciones.values(), 1): 
            print(f'{i}. {operacion.__name__}') #imprimir los tipos de kernel
        opcion = input('Ingrese la operacion: ')
        if 1 > int(opcion) or int(opcion) > 12: #si la opcion ingresada esta fuera del rango de opciones, muestra mensaje de error
            print("Operación inválida!")
            exit()

        if opcion == '1': 
            # aplica umbralizacion a la imagen utilizando la función umbralizacion del modulo 'f'
            imagen = f.umbralizacion(img_arr) 
            nombre_salida = f.nombre_salida()

        else:
            kernel = f.operaciones[opcion]()

            if len(img_arr.shape) == 2:  #verifica si la imagen es en escala de grises
                imagen = f.convolucion(img_arr, kernel)
                
            else: # para las imagenes RGB
                imagen = f.convolucion_rgb(img_arr, kernel)

            nombre_salida = f.nombre_salida()
        imagen = Image.fromarray(imagen) #Convierto el array en una imagen
        imagen.save(nombre_salida + '.png') #Guardo imagen con el nombre ingresado por el usuario en formato png

        print('Operacion realizada con exito!')

    except FileNotFoundError:
        print("Imagen no encontrada!")
        exit()

if __name__ == "__main__":
    main()