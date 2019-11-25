from PIL import Image


def window_to_display(window):
    dimensiones = len( window )
    display = [0 for i in range(1024)]
    for i in range( dimensiones[0] ):
        for j in range( dimensiones[1] ):
            modulo_j = j%8
            if modulo_j == 0:
                ubicacion = 16*j + i
            if window == 0:
                display[ ubicacion ] = 1 << ( modulo_j )
    return display

def bmp_to_display(file_path):
    display = [0 for i in range(1024)]

    imagen = Image.open( file_path )

    for i in range( imagen.size[0] ):
        for j in range( imagen.size[1] ):
            modulo_j = j%8
            if modulo_j == 0:
                ubicacion = 16*j + i
            if imagen.getpixel((i,j)) == 0:
                display[ ubicacion ] += 1 << ( modulo_j )



    return display