import warnings as alert

class Window:

    def __init__(self):
        self.window = [0 for i in range(1024)]
        

    def cargar_elemento(self, font, element_name, bit_inicial=[0, 0]):
        element = self.buscar_elemento(font, element_name)
        self.cargar_figura(element, bit_inicial)
        
    
    def buscar_elemento(self, font, element_name):
        if(type(font) != 'FontOled'):
            alert.warn('Se espera recibir una variable tipo Font')
        
        font_elements_names = font.letras
        existe = False
        for i in range(len(font_elements_names)):
            if font_elements_names[i] == element_name:
                existe = True
                break
        
        if ~existe:
            alert.warn('No se encontro el elemento esperado!')
        
        return font.get_letra(i)

    def cargar_figura(self, figure, bit_inicial):
        dimensiones = len( figure )
        for i in range( dimensiones[0] ):
            for j in range( dimensiones[1] ):
                self.window[i + bit_inicial[0]][j + bit_inicial[1]] = figure[i][j]
        
    