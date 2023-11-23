# Trabajo Practico 2 PC - La vida secreta de Peter Parker
## Introduccion
Usted es Peter Parker, un fotógrafo de un diario local reconocido. Su jefe, J. Jonah Jameson, es un poco paranóico de las herramientas 
de edición de fotos ya existentes, ya que cree que las fotos pueden ser robadas por los dueños de las herramientas. Por lo tanto,
le ha pedido que cree un programa que pueda realizar algunas operaciones básicas de procesamiento de imágenes.


Escriba un programa que le sugiera al usuario distintas opciones para el procesamiento de una imagen, 
tanto de umbralización como distintos kernels. La imagen resultante deberá guardarse en un archivo PNG

### Imágenes
Las imágenes se pueden representar como una matriz de pixeles, donde cada valor de la matriz representa el color del pixel en aquella posición. Por ejemplo, si estamos hablando de una imagen en escala de grises, la matriz sería en dos dimensiones (ancho y altura), y tendría valores entre 0 y 255. Donde un 0 correspondería al negro, y el 255 a el blanco, y los valores intermedios arman una escala de grises desde el negro al blanco.
![](https://udesa-pc.github.io/tps/tp2/img/grayscale.png)

En el caso de una imagen a color, la misma se representa por tres matrices, una por cada color básico (o canales), rojo, verde y azul 
(o RGB; red, green & blue) **Figura 2** 
Entonces, el color resultante de cada pixel será la combinación de los tres canales, cada uno definido con números entre 0 y 255, Figura 3. Por ejemplo, un pixel que tenga (255, 0, 0), es un pixel enteramente rojo. Y un pixel que tenga (72, 201, 176), es un pixel verde agua.

Por lo tanto, una imagen a color se representa como una matriz con tres dimensiones (ancho, altura y canal).

![](https://udesa-pc.github.io/tps/tp2/img/color_img_matrix.png)

### Edicion de imagenes
Cuando una persona o herramienta edita una imagen, lo que está haciendo es modificar los valores de esta matriz para que genere el efecto deseado
en la imagen. Por ejemplo, si uno quiere oscurecer una imagen, lo que hace es disminuir todos los valores de la matriz para que se acerquen más al
negro. O si alguien quiere hacer la imagen más rojiza, lo que haría sería aumentar los valores del canal rojo de todos los pixeles.

## OPERACIONES
### Umbralizacion 
El umbralizado (o thresholding) de una imagen es una operación que requiere un número (umbral), y lo que se hace es que todos 
los pixeles que tengan valores inferiores al umbral, se ponen en negro (0); y todos los pixeles que tengan valores 
superiores al umbral, se ponen en blanco (255). Por lo que, en una imagen en escala de grises, todos los pixeles quedarían en blanco o negro.

![](https://udesa-pc.github.io/tps/tp2/img/threshold.png)

Y para una imágen a color, el thresholding se hace canal a canal, por lo que todos los pixeles pasan a rojo (255,0,0), 
amarillo (255,255,0), verde (0,255,255), cyan (0,255,255), azul (0,0,255), magenta (255,0,255), blanco (255,255,255) o negro (0,0,0).

![](https://udesa-pc.github.io/tps/tp2/img/threshold_color.png)

Para una imagen a color se puede definir un umbral distinto para cada canal, o usar el mismo para todos los canales.
### Filtros de CONVOLUCION 
La convolución de matrices consiste en multiplicar elemento a elemento una matriz contra una parte de otra y sumar los resultados.

Tomando como ejemplo la Figura 6, cuando se ubica el kernel (filter) centrado sobre un elemento de la matriz (en este caso el de valor 2 [fila1, columna 1] de input)
quedan coincidiendo un elemento del kernel a un elemento de la matriz. Entonces, se multiplican los valores que coinciden entre sí y se suman los resultados.
El resultado final será una matriz output cuyo elemento ubicado en [fila 0, columna 0] se obtiene como: 
**2*1 + 1*2 + 1*0 + 4*0 + 2*0 + 5*2 + 3*0 + 5*2 + 7*2 = 38**
Tener en cuenta que la matriz de salida es mas chica por los efectos de borde (ver nota).

![](https://udesa-pc.github.io/tps/tp2/img/convolution.png)

En este caso, la matriz es una imágen, y al aplicar una convolución con distintos kernels generará “filtros” en
la imágen. Entonces, por ejemplo, si hacemos una convolución entre una imágen y el siguiente kernel:

|  -1   |  -2   |  -1   |
|----- |----- |----- |
|  0   |  0   |  0   |
|  1   |  2   |  1   |

Y finalmente, normalizamos la imágen resultante. Se obtendrá una imágen que resalta los bordes verticales de la 
imágen original. Este es lo que se conoce como un filtro de Sobel vertical.

![](https://udesa-pc.github.io/tps/tp2/img/sobel_vertical.png)


#### Normalizacion
Para normalizar una imágen, se debe calcular el mínimo y el máximo de la imágen, y luego aplicar la 
siguiente fórmula a cada pixel de la imágen: 

```math
\displaystyle 
    \frac{(pixel - min)}{{(max - min)}
        } * 255
```
#### Pixeles de borde
Cuando se ubica el kernel en uno de los pixeles de borde de la imágen se necesita rellenar los valores que no
coinciden con el kernel con algún valor. Se puede elegir rellenar con ceros, o con el valor de un pixel vecino
de la imágen.

### REQUERIMIENTOS DEL PROGRAMA
Escriba un programa que le sugiera al usuario distintas opciones para el procesamiento de una imagen, tanto de
umbralización como distintos kernels. La imagen resultante deberá guardarse en un archivo PNG.

Se debera sumar un:
**Kernel personalizado**
-> Si se selecciona esta opción, se le debe pedir al usuario el tamaño del kernel, y luego se le debe pedir que ingrese los valores del kernel. El tamaño del kernel debe ser un número impar, y los valores del kernel deben ser números enteros o flotantes.
