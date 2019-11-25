class Window:

    def __init__(self):
        self.window = [0 for i in range(1024)]

    def cargar_elemento(self, elemento, bit_fila_inicial, bit_columna_inicial):
        dimensiones = len( elemento )
        for i in range( dimensiones[0] ):
            for j in range( dimensiones[1] ):
                self.window[i + bit_fila_inicial][j + bit_columna_inicial] = elemento[i][j]