#Comentar: seleccionar el codigo a comentar y presionar Ctrl + K + C
#Comentar: seleccionar el codigo a comentar y presionar Ctrl + K + U
int_1 = 10
int_2 = 5
print(f"El valor de la variable int_1 es: {int_1}")
print(f"El valor de la variable int_2 es: {int_2}")
suma = int_1 + int_2
print(f"La suma de {int_1} + {int_2} es: {suma}")

resta = int_1 - int_2
print(f"La resta de {int_1} - {int_2} es: {resta}")

multiplicacion = int_1 * int_2
print(f"La multiplicacion de {int_1} * {int_2} es: {multiplicacion}")

division = int_1 / int_2 
print(f"La division de {int_1} / {int_2} es: {division}")

potencia = int_1 ** int_2   
print(f"La potencia de {int_1} ^ {int_2} es: {potencia}")

#variables strign
str_1 = "Hola"
str_2 = "Mundo"
print(f"La concatenacion de {str_1} + {str_2} es: {str_1 + str_2}") 

#Variables Listas

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]  
print(f"La concatenacion de {lista_1} + {lista_2} es: {lista_1 + lista_2}")
print(f"La suma de {lista_1} + {lista_2} es: {lista_1 + lista_2}")


Lista = [5,1,5,8,9,2,3,4,5,8]
#utiilizando .sort() para ordenar la lista
Lista.sort()
print(f"La lista ordenada es: {Lista}")

lista_2 = [200,50,20,100,40,500]
print (lista_2[2])


#python ordena la lista de cadena de texto de forma alfabetica
lista_3 = ['David' , 'Damaris' , 'Dario' , 'Daniel']
lista_3.sort()
print (lista_3)


#los diccionarios son estructuras de datos que almacenan pares de clave-valor 
#ejemplo, numero de cliente con sus datos
#en este caso el numero de cliente es la clave y el nombre es el valor
diccionario = { 125: 'David', 126: 'Damaris', 127: 'Dario', 128: 'Daniel'}
print(diccionario[129])