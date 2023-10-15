from PIL import Image #Para leer imagenes
import numpy as np #Para trabajar con arreglos (matrices)
import matplotlib.pyplot as plt  #Para mostrar la imagen
import funciones as f

def main():
    """
    Programa principal para llevar a cabo el procesamiento de las imagenes. Permite al usuario cargar la imagen (posteriormente visualizarla),
    y seleccionar una operación (donde se aplica la umbralizacion o la convolucion con distintos tipos de kernels). 

    Interacciones con el usuario:
    -----------------------------
    - El programa le solicita el nombre del archivo.
    -  La imagen se carga y posteriormente se muestra una lista con las distintas operaciones. 
    - El usuario debe ingresar el numero correspondiente de la operacion.
    - Para "Kernel personalizado" -- el usuario tiene la posibilidad de ingresar el tamaño y los valores del kernel. 
    - Despues de la selección, se solicita al usuario ingresar un nombre para el archivo de salida (formato PNG).
    - Se aplica la operacion a la imagen igresada, luego muestra el resultado. 

    Si el nombre del archivo no existe o el numero de la operacion ingresada no se ecuentra en la lista, se muestra 
    un mensaje de error y el programa termina. 
    """
    try:
        img_ing = input('Ingrese el nombre del archivo de la imagen: ')
        img = Image.open('test_images//' + img_ing)
        img_arr = np.array(img)
        
        plt.imshow(img_arr, cmap='gray')
        plt.show()

        nombre_salida = input('Ingrese el nombre del archivo de salida (SIN extension): ')
        while '.' in nombre_salida:
            nombre_salida = input('Nombre SIN extension: ')
        nombre_salida += '.png' #Para que sea en formato .png

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

        else:
            kernel = f.operaciones[opcion]()

            if len(img_arr.shape) == 2:  #verifica si la imagen es en escala de grises
                imagen = f.convolucion(img_arr, kernel)
                
            else: # para las imagenes RGB
                imagen = f.convolucion_rgb(img_arr, kernel)

        imagen = Image.fromarray(imagen) #Convierto el array en una imagen
        imagen.save(nombre_salida) #Guardo imagen con el nombre ingresado por el usuario

        print('Operacion realizada con exito!')

    except FileNotFoundError:
        print("Imagen no encontrada!")
        exit()

if __name__ == "__main__":
    main()