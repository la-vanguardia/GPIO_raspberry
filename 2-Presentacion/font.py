from PIL import Image
import display

class FontOled:

    def __init__(self, path = './Resource/Images/atascii.bmp'):
        self.font_matriz = display.bmp_to_display(path)

    def letra(self, letra):
        return self.font_matriz[ letra ]

        

        


