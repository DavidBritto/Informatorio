#Parametros:

# def prueba_parametros(nombre, it_obj, dic_obj, mensaje="Hola"):
#     print(f"Hola {nombre}")

#     for i in it_obj:
#         print(f"imprimiendo cada elemento de it_obj: {i}")
#         #Esto es un bucle que itera sobre cada elemento de it_obj y lo imprime.
#         #"{i}" significa que se imprimirá el valor de i en la cadena.
#     for k, v in dic_obj.items():
#         print(f"imprimiendo cada elemento de dic_obj: {k} : {v}")
#         #Esto es un bucle que itera sobre cada elemento de dic_obj y lo imprime.
#         #"{k}" significa que se imprimirá el valor de k en la cadena.
#         #"{v}" significa que se imprimirá el valor de v en la cadena.
# prueba_parametros ("David", [1, 2, 3, 4, 5], {1: 'uno', 2: 'dos', 3: 'tres'} )

# def prueba_parametros(nombre, mensaje="Hola", *it_obj, **dic_obj):
#     print(f"{mensaje} {nombre}")
#     """
#     Esta función recibe un nombre y un mensaje opcional, 
#     y luego imprime el mensaje seguido del nombre.
#     """
#     for i in it_obj:
#         print(f"imprimiendo cada elemento de *it_obj: {i}")

#     for k, v in dic_obj.items(): #{a: 'uno', b: 'dos', c: 'tres'} -->((a, 'uno'), (b, 'dos'), (c, 'tres'))
#         print(f"imprimiendo cada elemento de **dic_obj: {k} : {v}")
#         #Esto es un bucle que itera sobre cada elemento de dic_obj y lo imprime.
#         #"{k}" significa que se imprimirá el valor de k en la cadena.
#         #"{v}" significa que se imprimirá el valor de v en la cadena.
# prueba_parametros ("David", "Hola", 1, 2, 3, 4, 5, a='uno', b='dos', c='tres')
#En este caso, la función prueba_parametros recibe un nombre y un mensaje opcional.
#Estos parámetros son obligatorios y opcionales, respectivamente.
#Luego, la función imprime el mensaje seguido del nombre.

#El resto de los parámetros son opcionales y se pueden pasar como argumentos adicionales.
#La función también imprime cada elemento de it_obj y dic_obj.

#Se pueden cambiar los nombres de it_obj y dic_obj a cualquier otro nombre que desees.
#El nombre de los parámetros no afecta el funcionamiento de la función.
#El nombre de los parámetros es solo una convención y no afecta el funcionamiento de la función.
#Estos metodos sirven para recibir una cantidad variable de argumentos y almacenarlos en una tupla o diccionario.
# Y no estar escribiendo el mismo código una y otra vez.

#Ejemplo de uso de la función:

from traceback import print_tb


dividendo = 1024
divisor = 8

print(f"El modulo de {dividendo} y {divisor} es: {(dividendo / divisor)}")
#El resultado de la división es: 128.0
#Esto divide el dividendo entre el divisor y devuelve el resultado.
#pudiendo guardar el resultado en una variable y reutilizarla, en vez de reutilizar el mismo código.

def f(x): #f(x)=x**2 + 3.x + 10
    return x ** 2 + 3 * x + 10
#La función f toma un argumento x y devuelve el resultado de la expresión x**2 + 3.x + 10.
#La función f(x) es una función cuadrática
#Que toma un número x como argumento y devuelve el resultado de la expresión x**2 + 3.x + 10.

#f(1)=0**2 + 3*0 + 10 =
#      = 0 + 0 + 10 = 10
#f(1)=1**2 + 3*1 + 10 =
#      = 1 + 3 + 10 = 14
print (f(1))

barra =  ("----------------------------------------------------------------------------")
print (barra)
def mod(dividendo, divisor):
    return dividendo % divisor
def calculo(numeros): #numeros = [1,2,3,4,5,6,7,8,9,10]
    pares = []
    impares = []
    for i in numeros:
        modulo = mod(i, 2)
        if modulo == 0:
            pares.append(i)
        else:
            impares.append(i)
#Este código define una función llamada "calculo" que toma una lista de números como argumento.
#Dentro de la función, se crean dos listas vacías llamadas "pares" e "impares".
#Luego, se itera sobre cada número en la lista "numeros" y se calcula el módulo de cada número con 2.
#Si el resultado del módulo es 0, significa que el número es par y se agrega a la lista "pares".
# Si el resultado del módulo es 1, significa que el número es impar y se agrega a la lista "impares".
# Finalmente, la función devuelve las listas "pares" e "impares".
    print(f"el numero de pares es: {pares}")
    print(f"el numero de pares es: {impares}")
    print (barra)
pares = [32,123,55557, 123456, 123456789, 1234567890]
impares = [18,558,6698,55,69,69,45]

calculo([1,2,3,4,5,6,7,8,9,10,11,12,13,14])

print(f"Los números pares son: {pares}")
print(f"Los números impares son: {impares}")