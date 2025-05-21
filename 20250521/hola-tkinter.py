import tkinter as tk
import datetime

def saludar():
	print(datetime.datetime.now())

#clase es el molde o el formato de un objeto == instanciar o crear un objeto.
#Las clases tienen atributos y métodos.
#En este caso, la clase es una plantilla para crear objetos de tipo ventana.
ventana = tk.Tk()
ventana.title("Mi primera ventana con Tkinter")
ventana.geometry("800x600") #Ancho x Alto
#tk.label es un widget que se utiliza para mostrar texto o imágenes en la ventana.
texto = tk.Label(ventana, text="Hola, mundo!", font=("Arial", 24))
texto.pack()
#El método pack() es un método de diseño que coloca el widget en la ventana.
boton = tk.Button(ventana, text="Haz clic aquí", font=("Arial", 16), command=saludar)
boton.pack()
#El método command se utiliza para especificar la función que se ejecutará cuando se haga clic en el botón.
ventana.mainloop()