#El bucle for se utiliza para iterar sobre los elementos de un objeto iterable,
#como una lista, una cadena o un diccionario.
#Ejemplo de un diccionario:
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#Este bucle for itera sobre las claves del diccionario
#y las imprime en la consola.
#for clave in diccionario:
#    print(clave) 


#for valor in diccionario.values():
#    print(valor)   
 #Este bucle for itera sobre los valores del diccionario
# #y los imprime en la consola.
# 
#for key, value in diccionario.items():
#   print(key, value)
# # #Este bucle for itera sobre las claves y los valores del diccionario
# # #y los imprime en la consola.    

#Tarea:
#El usuario ingresa un string 'Hola' y el programa debe escribirlo al reves.
#No se puede usar el metodo reverse() ni el operador [::-1]
#Solo con Strnins y operaciones elemantales de concatenación.

cadena = input(' Ingresa una palabra: ')
invertida = ''
#El bucle for itera sobre cada letra de la cadena
#y la concatena a la variable invertida.

for letra in cadena:
    invertida = letra + invertida
#Esto devuelve una cadena con las letras invertidas
print(f"La cadena invertida se ve como: {invertida}")
#Verificamos si la cadena original es igual a la cadena invertida
#Si son iguales, la cadena es capicua/palindroma
if (invertida == cadena):
    print(f"La Palabra {cadena} es capicua/palindroma")
else:
    print(f"La Palabra {cadena} No es capicua/palindroma")  
#A este juego se le puede agregar un bucle while para que el usuario
#pueda ingresar varias palabras y el programa las verifique una por una.
#Con un metodo parecido a este podemos hacer un juego de adivinanza
#donde el usuario tiene que adivinar una palabra y el programa le dice
#si la palabra es correcta o no.
#El programa puede seguir pidiendo palabras hasta que el usuario
#decida salir.
#O bien podemos hacer un creador de contraseñas donde el usuario
#pueda ingresar palabras y numeros y el programa devuelva una contraseña
#aleatoria con esos elementos.
#Ejemplo de un creador de contraseñas:
