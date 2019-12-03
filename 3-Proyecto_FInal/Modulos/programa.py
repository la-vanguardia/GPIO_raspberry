import acelerometro
import ds18b20
import clock

acelerometro = acelerometro.Acelerometro(0x1C)
print( acelerometro.leerAceleraciones() )