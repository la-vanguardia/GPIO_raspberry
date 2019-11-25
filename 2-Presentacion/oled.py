import smbus

class DisplayOled:

    def __init__(self, codigo_familia = 0x3C, bus = 1):
        self.codigo_familia = 0x3C
        self.oled = smbus.SMBus(1)

    def iniciar_modulo(self):
        archivo_data = open('./Resouce/codes/cmd_comands.txt')
        data = []
        
        for comando in archivo_data:
            data.append( int( comando ) )
        
        archivo_data.close()

        self.configurar_modulo(data)
        self.borrar_pantalla()

    def configurar_modulo(self, data):
        self.oled.write_block_data( self.codigo_familia, 0x00 ,data )

    def cargar_display(self, display):
        for i in range(8):
            self.setear_pagina(i)
            for j in range(128):
                self.enviar_caracter(display[128*i + j])

    def borrar_pantalla(self):
        for i in range(8):
            self.setear_pagina(i)
            for j in range(128):
                self.enviar_caracter(0)
    
    def enviar_caracter(self, caracter):
        self.oled.write_byte_data(self.codigo_familia, 0x40, caracter)

    def setear_pagina(self, page):
        self.oled.write_byte_data(self.codigo_familia, 0x00, 0xB0 | (page & 0x0F) )
        self.oled.write_byte_data(self.codigo_familia, 0x00, 0x02)
        self.oled.write_byte_data(self.codigo_familia, 0x00, 0x10 | (0x01 >> 4))
    

















    


