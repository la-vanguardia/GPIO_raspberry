import oled
    

class OledInterface:

    def __init__(self, codigo_familia = 0x3C, bus = 1, resource_path= './Resource', relative_font_path = 'atascii.bmp'):
         self.displayOled = oled.DisplayOled(codigo_familia, bus)
         self.resource_path = resource_path
         self.font_relative_path = '/' + relative_font_path
        
         

