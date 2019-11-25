from PIL import Image
import display

class FontOled:

    def __init__(self, path = './Resource/Images/atascii.bmp'):
        self.font_matriz = display.bmp_to_display(path)
        

        ubicacion_fila = open('./letras.txt')

        self.letras = ubicacion_fila.read().split('\n')

        ubicacion_fila.close()

        


    def get_letra(self, letra):
        letra_oled = []
        ubicacion_letra = self.ubicacion_letra(letra)
        for i in range(8):
            letra_oled.append( self.font_matriz[ubicacion_letra + i ] )

        return letra_oled

    def ubicacion_letra(self, letra):
        for i in range( len(self.letras) ):
            if( self.letras[i] == letra ):
                return (i+3)*8

        

        


