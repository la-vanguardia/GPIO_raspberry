import window

class WindowsGenerator:

    def __init__(self):
        self.windows = []

    def crear_ventana(self):
        self.windows.append( window.Window() )

    def cargar_ventana(self, ubicacion, ventana):
        self.windows[ ubicacion ] = ventana

    