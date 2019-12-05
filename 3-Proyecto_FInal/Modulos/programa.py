import acelerometro
import ds18b20
import clock
from Final import *
from modulos import *
import ClienteMQTT as mqttClient

def leer_datos():
    hora = clock.devolver_hora()
    aceleraciones = sensor_acel.leerAceleraciones()
    temp = temperatura.tempC()
    mediciones = [aceleraciones, hora, temp]
    for medicion in mediciones:
        enviar_mensaje(cliente, medicion)

def mostrar_datos():
    print('hola')

def complemento_2_decimal(numero):
    numero_convertido = numero
    if numero>>7 == 1:
        numero_convertido = -1 * (numero & 0x7F)
    return numero_convertido



hora = [0x80,0x55,0x43,0x17,0x03,0x26,0x11,0x19]

#sensor_acel = acelerometro.Acelerometro(0x1C)
#clock = clock.Clock( hora )
#temperatura = ds18b20.DS18B20()
#print( acelerometro.leerAceleraciones() )
#print( clock.devolver_hora() )
#print( temperatura.tempC() )

tareas.append( Repetir(.5, enviar_dato) )
tareas.append( Repetir(1, mostrar_datos))

for tarea in tareas:
    tarea.start()

App.mainloop()                      #corremos la App
    