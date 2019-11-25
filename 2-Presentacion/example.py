import oled 
import display
import font
import window
import time.sleep as delay

displayOled = oled.DisplayOled()

displayExample = display.bmp_to_display('./Resource/Images/atascii.bmp')

displayOled.iniciar_modulo()

display = [0 for x in range(1024)]

fontVar = font.FontOled()
win = window.Window()

win.cargar_elemento(fontVar, 'flecha_arriba', [8,0])

win.cargar_elemento(fontVar, 'H', [0,0])

ubicaciones = fontVar.get_frase('Hola Buenas tardes!')


for j in range(len(ubicaciones)):
    letra = ubicaciones[j]
    for i in range(len(letra)):
        display[i + 8*j] = letra[i]

display_2 = display.window_to_display(win.window)

displayOled.cargar_display( display )

delay(1)

displayOled.cargar_display( display_2 )