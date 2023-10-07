import numpy as np

def kernel_personalizado (n):
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

n = int(input("Ingrese el tamaño del kernel: "))

while n % 2 == 0:
    n = int(input("Ingrese el tamaño del kernel: "))
    
filtro = kernel_personalizado(n)
print(filtro)

