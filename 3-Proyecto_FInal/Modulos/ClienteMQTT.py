import paho.mqtt.client as mqtt

datos = {
    'Grupo_1': [0, 0, 0, 0, 0, 0,0 ]

}


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Conexion: "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic='lauti_isa', qos=2)
    
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(str(msg.payload))

def crear_cliente(client_name="Lauti_Isa", host='127.0.0.1', port=1883):
    client = mqtt.Client(client_id= client_name, clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host= host, port= port)
    return client

def conectar_servidor(client):
    client.loop_start()

def enviar_mensaje(client, mensaje):
    client.publish(topic='lauti_isa', payload=mensaje, qos=2, retain=False)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
