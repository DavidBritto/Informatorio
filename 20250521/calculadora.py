from tkinter import font
import tkinter as tk

#LA V2 DEL EJERCICIO ESTA ABAJO 
# Definición de funciones para las operaciones

# def calcular_suma():
#     print(entrada)
#     expresion = entrada.get()
#     print(expresion)
#     try:
#         if all(char in "0123456789+-*/" for char in expresion):
#             resultado = eval(expresion)
#             resultado_var.set(f"Resultado: {resultado}")
#         else:
#             resultado_var.set("Error: Solo se permiten números y operadores +, -, *, /")
#     except:
#         resultado_var.set("Error en la expresión")

# def calcular_resta():
#     expresion = entrada.get()
#     try:
#         if all(char in "0123456789+-*/" for char in expresion):
#             resultado = eval(expresion)
#             resultado_var.set(f"Resultado: {resultado}")
#         else:
#             resultado_var.set("Error: Solo se permiten números y operadores +, -, *, /")
#     except:
#         resultado_var.set("Error en la expresión")

# def calcular_multiplicacion():
#     expresion = entrada.get()
#     try:
#         if all(char in "0123456789+-*/" for char in expresion):
#             resultado = eval(expresion)
#             resultado_var.set(f"Resultado: {resultado}")
#         else:
#             resultado_var.set("Error: Solo se permiten números y operadores +, -, *, /")
#     except:
#         resultado_var.set("Error en la expresión")

# def calcular_division():
#     expresion = entrada.get()
#     try:
#         if all(char in "0123456789+-*/" for char in expresion):
#             resultado = eval(expresion)
#             resultado_var.set(f"Es igual a: {resultado}")
#         else:
#             resultado_var.set("Error: Solo se permiten números y operadores +, -, *, /")
#     except:
#         resultado_var.set("Error en la expresión")

#Definición de calculadora V2
def calcular():
    #entrada.get es para obtener el texto ingresado en la entrada y guardarlo en la variable expresion
    expresion = entrada.get()
    try:
        if all(char in "0123456789+-*/" for char in expresion):
            #eval es una función que evalua una expresión matemática, es peligrosa si se usa con datos no confiables.
            resultado = eval(expresion)
            resultado_var.set(f"Es igual a {resultado}")
        else:
            resultado_var.set("Error: Solo se permiten números y operadores +, -, *, /")
    except:
        resultado_var.set("Error en la expresión")

def limpiar():
    entrada.set("")
    resultado_var.set("")

#Ventana

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")

entrada = tk.StringVar()
resultado_var = tk.StringVar()

tk.Label(ventana, text="Ingresa una expresión Ej: 4 + 3").pack(pady=10)
tk.Entry(ventana, textvariable=entrada, font=("Arial", 14), justify="center").pack(pady=5)
#Tk.label es para mostrar un texto en la ventana
#tk.entry es para ingresar un texto en la ventana
tk.Label(ventana, textvariable=resultado_var, font=("Arial", 14),).pack(pady=10)
#Alinear los botones hacia la izquierda
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)
tk.Button(frame_botones, text="Calcular", command=calcular).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botones, text="Limpiar", command=limpiar).pack(side=tk.LEFT, padx=5)

ventana.mainloop()
