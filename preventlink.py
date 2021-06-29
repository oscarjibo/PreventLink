from tkinter import * #Importamos tkinter para nuestra interfáz gráfica
import socket #Importamos la librería socket para poder comunicarnos con nuestro ESP8266
import threading # lib multihilo
import tkinter as tk
# espacios
padX=20
padY=30

ESP_IP = '192.168.1.7'  #IP de nuestro modulo
ESP_PORT = 8266#Puerto que hemos configurado para que abra el ESP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #objeto socket
s.connect((ESP_IP , ESP_PORT)) #Nconectarnos
root=Tk() # ventana
root.title("control leds por wifi O jimenez ") #Ctitutlo
tempVar=StringVar()
humVar=StringVar()
datos= {'temperatura:': tempVar,'humedad:': humVar}# diccionario
frame = Frame(root)  # ventanita

lbl_titulo = Label(frame, text="control led jimenez")  # titulito
imagenESP = PhotoImage(file="esp8266.png") #subir imagen
lbl_imagen = Label(frame, image=imagenESP) #poner img

lbl_titulo.grid(row=0, column=0, pady=padY,padx=padX)  #
lbl_imagen.grid (row=0, column=1,columnspan=2,pady=padY,padx=padX) #




lbl_LEDControl = Label (frame, text="Control Motor")
lbl_LEDControl.grid (row=1, column=0)
lbl_LEDControl1 = Label (frame, text="Control LED2")
lbl_LEDControl1.grid (row=3, column=0)
lbl_LEDControl2 = Label (frame, text="Control LED3")
lbl_LEDControl2.grid (row=5, column=0)

# funciones de encender
def enciendeLED():              #Función para encender el LED
    print("Encendiendo LED")
    dato = '1'
    s.send(dato.encode(encoding='utf_8'))  #enviamos 1 al modulo

def apagaLED():
    print("Apagando LED")
    dato = '0'
    s.send(dato.encode(encoding='utf_8'))
def enciendeLED2():
    print("Encendiendo LED")
    dato = '2'
    s.send(dato.encode(encoding='utf_8'))

def apagaLED2():
    print("Apagando LED")
    dato = '3'
    s.send(dato.encode(encoding='utf_8'))
def enciendeLED3():
    print("Encendiendo LED")
    dato = '4'
    s.send(dato.encode(encoding='utf_8'))

def apagaLED3():
    print("Apagando LED")
    dato = '5'
    s.send(dato.encode(encoding='utf_8'))


btn_LEDOn = Button(frame, text="On", fg="green", command=enciendeLED)  
btn_LEDOff = Button(frame, text="Off", fg="red",command=apagaLED)      

btn_LEDOn2 = Button(frame, text="On", fg="green", command=enciendeLED2)
btn_LEDOff2 = Button(frame, text="Off", fg="red",command=apagaLED2)

btn_LEDOn3= Button(frame, text="On", fg="green", command=enciendeLED3)
btn_LEDOff3 = Button(frame, text="Off", fg="red",command=apagaLED3)


btn_LEDOn.grid (row=1, column=1,pady=padY)                                                     
btn_LEDOff.grid (row=1, column=2,pady=padY)     

btn_LEDOn2.grid (row=3, column=1,pady=padY)     
btn_LEDOff2.grid (row=3, column=2,pady=padY)    

btn_LEDOn3.grid (row=5, column=1,pady=padY)      
btn_LEDOff3.grid (row=5, column=2,pady=padY)    

lbl_temp=tk.Label(frame, textvariable=tempVar) ## etiqueta temp
lbl_hum=tk.Label(frame, textvariable=humVar)
lbl_temp.grid(row=11,column=0, padx=padX,pady=padY)
lbl_hum.grid(row=11,column=1, padx=padX,pady=padY)

def recibedatos():
    while True:
        cadena=s.recv(1023)
        print(cadena)
        lineas=cadena.splitlines()
        for linea in lineas:
            dato=linea.split()
            datos[dato[0].decode()].set(dato[0].decode()+" "+dato[1].decode())
hiloRecepcion=threading.Thread(target=recibedatos)
hiloRecepcion.start()
frame.pack()
root.mainloop()
