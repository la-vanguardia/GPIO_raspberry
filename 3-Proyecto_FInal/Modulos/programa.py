import acelerometro
import ds18b20
import clock
from Final import *
<<<<<<< HEAD
from ClienteMQTT import *
import json
=======
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


>>>>>>> 703ebda82eb3daf976ddac209ae3b5be772f9fb6


<<<<<<< HEAD
Group_1_datos = [
    'XX': TextBoxXXUno,
    'YY': TextBoxYYUno,
    'ZZ': TextBoxZZUno,
    'FechaHora': TextBoxFechaHoraUno,
    'Temperatura': TextBoxTempUno
]

Group_2_datos = [
    'XX': TextBoxXXDos,
    'YY': TextBoxYYDos,
    'ZZ': TextBoxZZDos,
    'FechaHora': TextBoxFechaHoraDos,
    'Temperatura': TextBoxTempDos
]

Group_3_datos = [
    'XX': TextBoxXXTres,
    'YY': TextBoxYYTres,
    'ZZ': TextBoxZZTres,
    'FechaHora': TextBoxFechaHoraTres,
    'Temperatura': TextBoxTempTres
]

Group_4_datos = [
    'XX': TextBoxXXCuatro,
    'YY': TextBoxYYCuatro,
    'ZZ': TextBoxZZCuatro,
    'FechaHora': TextBoxFechaHoraCuatro,
    'Temperatura': TextBoxTempCuatro
]

Groups_text_box = {
    'Grupo_1': Group_1_datos,
    'Grupo_2': Group_2_datos,
    'Grupo_3': Group_3_datos,
    'Grupo_4': Group_4_datos,
}

mediciones = {
    'XX': [0, 0],
    'YY': [0, 0],
    'ZZ': [0, 0],
    'FechaHora': [0, 0, 0, 0, 0, 0],
    'Temperatura': 0
}

def actualizar_mediciones():
    datos_aceleraciones = sensor_aceleraciones.leerAceleraciones()
    hora = clock.devolver_hora()
    datos_temperatura = temperatura.tempC()
    
    mediciones['XX'] = datos_aceleraciones[:1]
    mediciones['YY'] = datos_aceleraciones[2:3]
    mediciones['ZZ'] = datos_aceleraciones[3:]
    mediciones['FechaHora'] = hora
    mediciones['Temperatura'] = datos_temperatura

    enviar_mensaje( cliente, json.dumps(mediciones) )
    datos[my_topic] = mediciones

def actualizar_valores():
    for group in datos:
        for medicion in datos[group]:
            dato = clasificarMedicion(medicion, datos[group][medicion])
            Groups_text_box[group][medicion].delete(0, END)
            Groups_text_box[group][medicion].insert(0, str(dato))

def clasificarMedicion(medicion, dato):
    value = 0
    if medicion in ['XX', 'YY', 'ZZ']:
        value = complemento2(dato[0])*(16**2) + dato[1]
    elif medicion == 'FechaHora':
        pass
    elif medicion == 'Temperatura':
        pass
    return value

def complemento2(dato):
    number = dato
    if dato >> 7 == 1:
        number = -1 * (dato & 0x7F)
    return number

hora = [0x01,0x06,0x00,0x17,0x03,0x06,0x12,0x19]

sensor_aceleraciones = acelerometro.Acelerometro(0x1C)
clock = clock.Clock( hora )
temperatura = ds18b20.DS18B20()

tareas.append( Repetir(1, actualizar_mediciones) )
tareas.append( Repetir(.1, actualizar_valores))
=======
#sensor_acel = acelerometro.Acelerometro(0x1C)
#clock = clock.Clock( hora )
#temperatura = ds18b20.DS18B20()
#print( acelerometro.leerAceleraciones() )
#print( clock.devolver_hora() )
#print( temperatura.tempC() )

tareas.append( Repetir(.5, enviar_dato) )
tareas.append( Repetir(1, mostrar_datos))
>>>>>>> 703ebda82eb3daf976ddac209ae3b5be772f9fb6

for tarea in tareas:
    tarea.start()

<<<<<<< HEAD
App.mainloop()
=======
App.mainloop()                      #corremos la App
    
>>>>>>> 703ebda82eb3daf976ddac209ae3b5be772f9fb6
