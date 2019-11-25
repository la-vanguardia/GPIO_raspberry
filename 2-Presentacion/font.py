from PIL import Image
import display

class FontOled:

    def __init__(self, path = './Resource/Images/atascii.bmp'):
        self.font_matriz = display.bmp_to_display(path)

    def get_letra(self, letra):
        letraOled = []
        for i in range(8):
            for j in range(8):
                letraOled.append( self.font_matriz[letra + i +j] )

        return letraOled

        

        


