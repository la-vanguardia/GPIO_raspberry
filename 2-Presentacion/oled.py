import smbus
import time


codigo_familia = 0x78
oled = smbus.SMBus(1)

def enviar_byte(byte):
    oled.write_byte_data(codigo_familia , 0x00, byte)

def configurar_i2c():
    enviar_byte(0xAE)

    enviar_byte(0xA8)
    enviar_byte(0x3F)
    
    enviar_byte(0xD3)
    enviar_byte(0x00)

    enviar_byte(0x40)

    enviar_byte(0xA1)

    enviar_byte(0xC8)

    enviar_byte(0xDA)
    enviar_byte(0x12)

    enviar_byte(0x81)
    enviar_byte(0x7F)

    enviar_byte(0xA4)
    enviar_byte(0xA6)

    enviar_byte(0xD5)
    enviar_byte(0x80)

    enviar_byte(0x8D)
    enviar_byte(0x14)

    enviar_byte(0xAF)

    enviar_byte(0x21)
    enviar_byte(0x00)
    enviar_byte(0x7f)
    enviar_byte(0x22)
    enviar_byte(0x00)
    enviar_byte(0x07)

    enviar_byte(0x20)
    enviar_byte(0x00)

def enviar_bytes(display):
    for byte in display:
        enviar_byte(byte)

configurar_i2c()

for i in range(8):
    enviar_byte(0x40)
    enviar_byte(0x81)

















    


