#Comentar: seleccionar el codigo a comentar y presionar Ctrl + K + C
#Cescomentar: seleccionar el codigo a comentar y presionar Ctrl + K + U
# SINTAXIS BÁSICA EN PYTHON: VARIABLES, TIPOS DE DATOS Y OPERADORES

# -------------------------------------------
# VARIABLES:
# En Python, una variable es un nombre que se refiere a un valor.
# Se crean en el momento en que les asignas un valor por primera vez.
# No necesitas declarar su tipo de antemano (tipado dinámico).
# Los nombres de variables deben seguir ciertas reglas:
#   - Pueden contener letras, números y guiones bajos (_).
#   - No pueden empezar con un número.
#   - Son sensibles a mayúsculas y minúsculas (edad es diferente de Edad).
#   - No pueden ser palabras reservadas de Python (como if, for, class, etc.).

# Ejemplo de creación de variables:
nombre_completo = "Juan Pérez"  # Variable de tipo cadena (string)
edad = 30                     # Variable de tipo entero (integer)
altura_metros = 1.75          # Variable de tipo flotante (float)
es_estudiante = False         # Variable de tipo booleano (boolean)

# Podemos imprimir los valores de las variables y su tipo con:
# print("Nombre:", nombre_completo, "- Tipo:", type(nombre_completo))
# print("Edad:", edad, "- Tipo:", type(edad))
# print("Altura:", altura_metros, "- Tipo:", type(altura_metros))
# print("Es estudiante:", es_estudiante, "- Tipo:", type(es_estudiante))

# Se puede reasignar un valor (y por lo tanto, el tipo) a una variable:
# edad = "Treinta años"
# print("Nueva Edad:", edad, "- Nuevo Tipo:", type(edad))

# -------------------------------------------
# TIPOS DE DATOS BÁSICOS:
# Python tiene varios tipos de datos incorporados. Los más comunes son:

# 1. Enteros (int): Números sin decimales.
#    Ej: numero_entero = 100
#        otro_entero = -50

# 2. Flotantes (float): Números con decimales.
#    Ej: numero_flotante = 3.1416
#        precio_producto = 99.99

# 3. Cadenas de Texto (str): Secuencias de caracteres, entre comillas simples o dobles.
#    Ej: saludo = 'Hola Mundo'
#        descripcion = "Python es un lenguaje de programación."
#        # Las cadenas se pueden concatenar (unir)
#        mensaje_completo = saludo + " - " + descripcion
#        # print(mensaje_completo)

# 4. Booleanos (bool): Representan valores de verdad, solo pueden ser True o False.
#    Ej: tiene_permiso = True
#        es_mayor_de_edad = False # (si edad < 18)

# 5. Nulo (NoneType): Representa la ausencia de valor. Se usa el valor 'None'.
#    Ej: valor_indefinido = None
#        # print("Valor indefinido:", valor_indefinido, "- Tipo:", type(valor_indefinido))

# Pequeña Práctica con Tipos de Datos:
# 1. Crea una variable para tu nombre y otra para tu edad.
# mi_nombre = "David"
# mi_edad = 28
# print(f"Hola, me llamo {mi_nombre} y tengo {mi_edad} años.") # f-string para formatear

# 2. Crea una variable que represente el precio de un café (con decimales).
# precio_cafe = 150.75
# print(f"El precio del café es: ${precio_cafe}")

# 3. Crea una variable booleana que indique si te gusta programar.
# me_gusta_programar = True
# print(f"¿Me gusta programar? {me_gusta_programar}")


# -------------------------------------------
# OPERADORES:
# Los operadores son símbolos especiales que realizan operaciones sobre valores y variables.

# 1. Operadores Aritméticos:
#    Suma: +
#    Resta: -
#    Multiplicación: *
#    División: / (siempre devuelve un flotante)
#    División Entera: // (devuelve la parte entera del cociente)
#    Módulo (resto de la división): %
#    Potencia: **

# Ejemplo de operadores aritméticos:
# num1 = 10
# num2 = 3
# print(f"{num1} + {num2} = {num1 + num2}")        # Suma: 13
# print(f"{num1} - {num2} = {num1 - num2}")        # Resta: 7
# print(f"{num1} * {num2} = {num1 * num2}")        # Multiplicación: 30
# print(f"{num1} / {num2} = {num1 / num2}")        # División: 3.333...
# print(f"{num1} // {num2} = {num1 // num2}")      # División Entera: 3
# print(f"{num1} % {num2} = {num1 % num2}")        # Módulo: 1
# print(f"{num1} ** {num2} = {num1 ** num2}")      # Potencia: 1000

# 2. Operadores de Comparación (Relacionales):
#    Igual a: ==
#    Distinto de: !=
#    Mayor que: >
#    Menor que: <
#    Mayor o igual que: >=
#    Menor o igual que: <=
#    Estos operadores devuelven un valor booleano (True o False).

# Ejemplo de operadores de comparación:
# a = 5
# b = 10
# print(f"{a} == {b}? {a == b}")     # False
# print(f"{a} != {b}? {a != b}")     # True
# print(f"{a} > {b}? {a > b}")      # False
# print(f"{a} < {b}? {a < b}")      # True
# print(f"{a} >= 5? {a >= 5}")    # True
# print(f"{b} <= 5? {b <= 5}")    # False

# 3. Operadores Lógicos:
#    AND lógico: and (True si ambos operandos son True)
#    OR lógico: or  (True si al menos uno de los operandos es True)
#    NOT lógico: not (Invierte el valor booleano)

# Ejemplo de operadores lógicos:
# condicion1 = True
# condicion2 = False
# print(f"{condicion1} and {condicion2}? {condicion1 and condicion2}") # False
# print(f"{condicion1} or {condicion2}? {condicion1 or condicion2}")   # True
# print(f"not {condicion1}? {not condicion1}")                      # False

# 4. Operadores de Asignación:
#    Asignación simple: =
#    Asignación con suma: +=  (ej: x += 1  es igual a x = x + 1)
#    Asignación con resta: -=
#    Asignación con multiplicación: *=
#    Asignación con división: /=
#    Y así con los demás operadores aritméticos (//=, %=, **=)

# Ejemplo de operadores de asignación:
# contador = 0
# # print("Contador inicial:", contador)
# contador += 5  # contador ahora es 5
# # print("Contador += 5:", contador)
# contador *= 2  # contador ahora es 10
# # print("Contador *= 2:", contador)

# Pequeña Práctica con Operadores:
# 1. Declara dos variables numéricas y calcula su suma, producto y quién es mayor.
# val1 = 25
# val2 = 15
# suma_vals = val1 + val2
# prod_vals = val1 *