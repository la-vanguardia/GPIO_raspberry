ubicacion_fila = open('./letras.txt')

letras = ubicacion_fila.read().split('\n')

for letra in letras:
    print(letra)