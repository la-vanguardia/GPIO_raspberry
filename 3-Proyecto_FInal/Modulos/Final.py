from tkinter import *               #importamos librería para generar interfaz gráfica
from tkinter import messagebox
from tkinter.ttk import *
from modulos import *
import ClienteMQTT as mqttClient
#from threading import Thread, Event
#from time import sleep

            
def Tarea():                               #definimos Tarea()
    print ("Ejecutar Tarea\n")
    
def TareaDos():
    print ("Ejecutar TareaDos\n")          #definimos TareaDos()

def enviar_dato():
    print('hola!')     

def ClickBotonConectar():                   #definimos click boton conectar
    if BotonConectar["text"]=="Conectar":
        BotonConectar["text"]="Desconec."
        TextBoxXXDos.delete(0,END)
        TextBoxXXDos.insert(0,25) 
    else:
        BotonConectar["text"]="Conectar"
        TextBoxXXDos.delete(0,END)
        TextBoxXXDos.insert(0,50)
      
def ClickBotonSalir(temporizadores= []):                      #definimos el evento click boton salir
    Eleccion=messagebox.askokcancel(message="¿Seguro que desea salir?",title="Pregunta")
    if Eleccion == True:
        for temp in temporizadores:
            temp.join()
            temp.stop()
        App.destroy()

######## creamos la ventana principal###########
TamañoEtiqueta = 10
TamañoTextBoxChico = 5
TamañoTextBoxMedio = 10
TamañoTextBoxGrande = 15

App = Tk()                              #generamos la interfaz    
App.title("Visualizador MQTT Cliente")  #establecemos el título de la App
App.geometry('790x105+200+200')                 #tamaño de la App
App.resizable(False,False)              #bloqueamos el tamaño de la App
######## fin ventana principal#########

######## inicio etiquetas######
EtiquetaParametros = Label(App,text="Parámetros//Grupos",font=("",TamañoEtiqueta))  #creamos una etiqueta
EtiquetaParametros.place(x=0, y=0)                                                 #ubicamos la etiqueta

EtiquetaG1 = Label(App,text="Uno",font=("",TamañoEtiqueta))
EtiquetaG1.place(x=175,y=0)     

EtiquetaG2 = Label(App,text="Dos",font=("",TamañoEtiqueta))
EtiquetaG2.place(x=315,y=0)  

EtiquetaG3 = Label(App,text="Tres",font=("",TamañoEtiqueta))
EtiquetaG3.place(x=455,y=0)

EtiquetaG4 = Label(App,text="Cuatro",font=("",TamañoEtiqueta))
EtiquetaG4.place(x=590,y=0)

EtiquetaAcel = Label(App,text="Aceleraciones",font=("",TamañoEtiqueta))
EtiquetaAcel.place(x=0,y=25)

EtiquetaTemp = Label(App,text="Temperatura",font=("",TamañoEtiqueta))
EtiquetaTemp.place(x=0,y=50)

EtiquetaFechaHora = Label(App,text="Fecha&Hora",font=("",TamañoEtiqueta))
EtiquetaFechaHora.place(x=0,y=75)
######## fin etiquetas#########

######inicio texbox grupo 1#######
TextBoxXXUno = Entry(App,width=TamañoTextBoxChico,justify=CENTER) #generamos un textbox
TextBoxXXUno.place(x=125,y=25)                                    #ubicamos el textbox
TextBoxXXUno.insert(5,80)                                         #insertamos un valor

TextBoxYYUno = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxYYUno.place(x=170,y=25)  

TextBoxZZUno = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxZZUno.place(x=215,y=25)

TextBoxTempUno = Entry(App,width=TamañoTextBoxMedio,justify=CENTER)         
TextBoxTempUno.place(x=150,y=50)

TextBoxFechaHoraUno = Entry(App,width=TamañoTextBoxGrande,justify=CENTER)         
TextBoxFechaHoraUno.place(x=130,y=75)
######fin texbox grupo 1#######

######inicio texbox grupo 2#######
TextBoxXXDos = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxXXDos.place(x=265,y=25)

TextBoxYYDos = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxYYDos.place(x=310,y=25)

TextBoxZZDos = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxZZDos.place(x=355,y=25)

TextBoxTempDos = Entry(App,width=TamañoTextBoxMedio,justify=CENTER)         
TextBoxTempDos.place(x=290,y=50)

TextBoxFechaHoraDos = Entry(App,width=TamañoTextBoxGrande,justify=CENTER)         
TextBoxFechaHoraDos.place(x=270,y=75)
######fin texbox grupo 2#######

######inicio texbox grupo 3#######
TextBoxXXTres = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxXXTres.place(x=405,y=25)

TextBoxYYTres = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxYYTres.place(x=450,y=25)

TextBoxZZTres = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxZZTres.place(x=495,y=25)

TextBoxTempTres = Entry(App,width=TamañoTextBoxMedio,justify=CENTER)         
TextBoxTempTres.place(x=430,y=50)

TextBoxFechaHoraTres = Entry(App,width=TamañoTextBoxGrande,justify=CENTER)         
TextBoxFechaHoraTres.place(x=410,y=75)
######fin texbox grupo 3#######

######inicio texbox grupo 4#######
TextBoxXXCuatro = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxXXCuatro.place(x=545,y=25)

TextBoxYYCuatro = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxYYCuatro.place(x=590,y=25)

TextBoxZZCuatro = Entry(App,width=TamañoTextBoxChico,justify=CENTER)         
TextBoxZZCuatro.place(x=635,y=25)

TextBoxTempCuatro = Entry(App,width=TamañoTextBoxMedio,justify=CENTER)         
TextBoxTempCuatro.place(x=570,y=50)

TextBoxFechaHoraCuatro = Entry(App,width=TamañoTextBoxGrande,justify=CENTER)         
TextBoxFechaHoraCuatro.place(x=550,y=75)
######fin texbox grupo 4#######


###### creamos los dos botones#########
BotonConectar = Button(App,text="Conectar",command =ClickBotonConectar) #creamos un boton
BotonConectar.place(x=700,y=20)        #ubicamos el boton
BotonSalir = Button(App,text="Salir",command =ClickBotonSalir) #creamos un boton
BotonSalir.place(x=700,y=70)          #ubicamos el boton
###### fin dos botones ################


tareas = []

tareas.append( Repetir(1, enviar_dato) )

cliente = mqttClient.crear_cliente()
mqttClient.conectar_servidor( cliente )

mqttClient.enviar_mensaje(cliente, 'HOLA!')

App.mainloop()                      #corremos la App
    