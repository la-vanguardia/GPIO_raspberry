import smbus as I2C

class Acelerometro:

    def __init__(self, codigo_familia):
        self.codigo_familia = codigo_familia
        self.acelerometro = I2C.SMBus(1)
        try:
            self.enviarDato(0x2A, 0x00)
            self.enviarDato(0x00, 0x2D)
            self.enviarDato(0x2A, 0x01)
        except:
            print('Conecte el dispositivo')


    def leerAceleraciones(self):
        aceleraciones =  self.acelerometro.read_i2c_block_data(self.codigo_familia, 0x01, 6) 
        return aceleraciones
    
    def enviarDato(self, registro, dato):
        self.acelerometro.write_byte_data(self.codigo_familia, registro, dato)

        
    

