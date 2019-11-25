import oled 
import display
import font

displayOled = oled.DisplayOled()

displayExample = display.bmp_to_display('./Resource/Images/atascii.bmp')

displayOled.iniciar_modulo()

display = [0 for x in range(1024)]

fontVar = font.FontOled()

letra = fontVar.get_frase('Hola pibe! @')

for i in range(len(letra)):
    display[i] = letra[i]

displayOled.cargar_display( display )