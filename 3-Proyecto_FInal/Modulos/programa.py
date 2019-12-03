import acelerometro
import ds18b20
import clock

hora = [0x80,0x55,0x43,0x17,0x03,0x26,0x11,0x19]

acelerometro = acelerometro.Acelerometro(0x1C)
clock = clock.Clock( hora )
temperatura = ds18b20.DS18B20()
print( acelerometro.leerAceleraciones() )
print( clock.devolver_hora() )
print( temperatura.tempC() )