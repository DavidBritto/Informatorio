#las listas en python son un tipo de dato que permite almacenar
#  una coleccion de elementos, pueden ser de diferentes tipos
#  y son mutables, es decir, se pueden modificar.

#Ejemplo de una lista:
# lista_1 = ['String', 1, 2.5, False]

# lista_2 = [1, 2, 3, 4, 5]

# lista_3 = ['Juan' , 'Pedro', 'Maria', 'Jose']

# print(lista_1)
# print(lista_2)
# print(lista_3)

#Se pueden crear listas vacias, listas con un solo elemento
# o listas con varios elementos.

#Ejemplo de una lista vacia:
# lista_vacia = []

#para agregar elementos a una lista se utiliza el metodo append()
#Ejemplo de agregar elementos a una lista:

# lista_1.append('Float')
# lista_2.append(6)
# lista_3.append('Ana')

# print('luego de agregar elementos a la lista')
# print(lista_1)
# print(lista_2)
# print(lista_3)

#Caso contrario con el metodo remove() se pueden eliminar elementos de una lista
#Ejemplo de eliminar elementos de una lista:
# lista_1.remove('String')
# lista_2.remove(1) 
# lista_3.remove('Juan')
# print('luego de eliminar elementos de la lista')

#Con el metodo True se pueden hacer verificaciones
#Ejemplo de verificacion:

#lista_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#verificar si un numero es mayor que 4.
# lista_nueva = [True for x in lista_4 if x > 4]
#Esto devuelve una lista con los elementos que cumplen la condicion
#de ser mayor que 4.
# print(lista_nueva)
#print(lista_4)
#Ademas podemos agregar el metodo else para verificar en sentido contrario:
#lista_nueva = [True if x > 4 else False for x in lista_4]
#Esto devuelve una lista con los elementos que cumplen la condicion
#de ser mayor que 4 como true y los que no cumplen como false.
#print(lista_nueva)

#Podemos usar reversed para invertir una lista
#lista_4.reverse()
#Esto devuelve una lista con los elementos invertidos
#print(lista_4)

#-------------------------------------------
#Tuplas:
#Las Tuplas son un tipo de dato que permite almacenar
#  una coleccion de elementos, pueden ser de diferentes tipos 
# pero son inmutables

#tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#print(tupla)
#tupla[0] = 2
#Esto devuelve un error porque las tuplas son inmutables
#En cambio si:
#tupla = ( [100], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#print(tupla)
#tupla[0][0] = 'caca'
#print(tupla)

#Esto devuelve una tupla con el primer elemento cambiado, ya que dentro
# de la tupla hay una lista que es mutable.
#Con el primer [0] accedemos a la lista 
# y con el segundo [0] accedemos al primer elemento de la lista.
#-------------------------------------------    
#Pregunta: ¿Puedo agregar elementos a una tupla, como una lista?
#Respuesta: No, no se pueden agregar elementos a una tupla, ya que son inmutables.
#Pero si se pueden agregar elementos a una lista dentro de una tupla.
#Como en el ejemplo anterior.
#Es lo mismo que manipular una lista, solo que esta dentro dentro de una tupla.
#Se puede transformar una tupla en una lista y viceversa.
#Ejemplo de transformar una tupla en una lista:

#lista = list(tupla)
#print(lista)

#De esta forma puedo agregar elementos a la lista

#lista.append(11)

#Y luego transformar la lista en una tupla de nuevo para garantizar la inmutabilidad
#tupla = tuple(lista)
#-------------------------------------------

#Conjuntos:
#Los conjuntos son utiles porque almacenan elementos unicos, no se repiten.
#Ejemplo de un comparador de conjunto:

#caja_1 = {'remera', 'pantalon', 'camisa'}
#caja_2 = {'remera', 'campera', 'medias', 'zapatos'}

#repetidos_en_cajas = caja_1 & caja_2
#print(repetidos_en_cajas)

#Ejemplo de una union de conjuntos:

#frutas = {'manzana', 'banana', 'naranja'}
#verduras = {'lechuga', 'tomate', 'zanahoria'}

#Unir los conjuntos

#ista_super = frutas | verduras
#print(lista_super)

#Podemos usar len para contar los elementos de un conjunto
#Ejemplo de contar los elementos de un conjunto:    

#len(lista_super)
#Esto devuelve la cantidad de elementos en el conjunto
#print(len(lista_super))
#-------------------------------------------

#Tarea:

#Crear una lista nueva con los elementos de la lista numbers
#  potenciados por si mismos:

#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#potenciados = [x ** x for x in numbers]
#print(potenciados)

#otra forma de hacerlo es:
#potenciados =[pow(x, x) for x in numbers]
#print(potenciados)

#Siendo pow la funcion que eleva un numero a otro.

#Crear una lista nueva con los elementos de la lista numbers
#  multiplicados por 2:
#multiplicados = [x*2 for x in numbers]
#print(multiplicados)

#Crear una lista nueva con los elementos de la lista numbers
#  multiplicados por 2 y sumados a 3:
#multiplicados_y_sumados = [(x*2) + 3 for x in numbers]
#print(multiplicados_y_sumados)

#poner la primer letra de cada palabra en mayuscula
lenguajes_programacion = ['python', 'java', 'swift', 'JavaScript', 'ruby']
lenguajes_mayusculas = [leng.upper() for leng in lenguajes_programacion]
print(lenguajes_mayusculas)

#Como vemos al ejecutar esto no cumple con la consigna.
#Para poner la primer letra de cada palabra en mayuscula
#podemos usar el metodo title() que pone la primer letra de cada palabra en mayuscula
lenguajes_mayusculas = [leng.title() for leng in lenguajes_programacion]
print(lenguajes_mayusculas)

#Otra forma de hacerlo es:

lenguajes_mayusculas = [leng[0].upper() + leng[1::] for leng in lenguajes_programacion]
print(lenguajes_mayusculas)

#Explicacion de la segunda forma:
#leng[0].upper() + leng[1::]
#Con esto accedemos a la primer letra de la palabra y la convertimos a mayuscula
#Con el segundo [1::] accedemos al resto de la palabra  
#Esto lo concatenamos con el + para formar la palabra completa
#-------------------------------------------
