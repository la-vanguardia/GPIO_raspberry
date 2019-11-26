import warnings as alert

class Window:

    def __init__(self):
        self.window = [0 for i in range(1024)]
        
    def cargar_elementos(self, font, frase, bit_inicial=0):
        frase = font.get_frase(frase)
        for letra in frase:
            self.cargar_figura(letra, bit_inicial)


    def cargar_elemento(self, font, element_name, bit_inicial=0):
        element = self.buscar_elemento(font, element_name)
        self.cargar_figura(element, bit_inicial)
        
    
    def buscar_elemento(self, font, element_name):
        return font.get_letra(element_name)

    def cargar_figura(self, figure, bit_inicial=0):
        dimensiones = len( figure )
        for i in range( dimensiones):
            self.window[i + bit_inicial] = figure[i]
    
    def cargar_texto_alineados(self, font, frase, alineacion='izquierda'):
        if alineacion == 'izquierda':
            self.cargar_elementos(font, frase)
        elif alineacion == 'derecha':
            self.cargar_elementos(font, frase, 16)
        elif alineacion == 'centrada':
            self.cargar_elementos(font, frase, 8)
        else:
            print('error')
        
    