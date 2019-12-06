import spidev


class Clock:

    def __init__(self, hora_inicial):
        self.spi = spidev.SpiDev()
        self.spi.open(0,1)
        self.spi.max_speed_hz = 312500
        self.spi.mode = 1
        self.spi.cshigh = True
        self.spi.xfer2([0x8F, 0x00])
        self.spi.xfer2( 0x80 + hora_inicial)

    def cambiar_hora(self, hora):
        self.spi.xfer2(0x80 + hora)

    def devolver_hora(self):
        datos = self.spi.xfer2( [0x00, 1, 2, 3, 4, 5, 6, 7] )
        del datos[4]
        del datos[0]
        datos[0], datos[2] = datos[2], datos[0]
        hora = self.hexa_to_dec(datos)
        return hora

    def hexa_to_dec(self, hex_numbers):
        dec_numbers = []
        for hex_number in hex_numbers:
            MSB_number = hex_number >> 4
            LSB_number = hex_number & 0x0F
            dec_numbers.append( MSB_number * 10 + LSB_number )
        return dec_numbers
    