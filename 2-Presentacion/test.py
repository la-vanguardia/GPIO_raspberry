ubicacion_fila = open('./letras.txt')

letras = ubicacion_fila.read().split('\n')

for i in range(len(letras)):
    if letras[i] == 'H':
        print(i + 1)