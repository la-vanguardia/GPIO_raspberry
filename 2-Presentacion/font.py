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

    def get_frase(self, frase):
        frase_separada = self.obtener_comandos(frase)
        ubicaciones = []
        for letra in frase_separada:
            ubicaciones.append( self.get_letra(letra) )

        return ubicaciones

    def ubicacion_letra(self, letra):
        for i in range( len(self.letras) ):
            if( self.letras[i] == letra ):
                return (i)*8

    def obtener_comandos(self, frase):
        comando_reconocido = False
        lista_comandos = []
        cmd = ''
        for letra in frase:
            if letra == '$':
                comando_reconocido = ~comando_reconocido
                if ~comando_reconocido:
                    lista_comandos.append(cmd)
                    cmd = ''
            else:
                if comando_reconocido:
                    cmd += letra
                else:
                    lista_comandos.append(letra)
        return lista_comandos
        

        


