#El usuario debe ingresar por pantalla una serie de numeros
#se debe sumar entre si la cadena ingresada, 
#Ejemplo: 99, el resultado es: 18.
#El usuario ingresa: 101 el resultado es: 2
#Se debe usar while y for 

numero = int(input("Ingresa un numero: "))

suma = 0

while numero > 0:
    #El operador % devuelve el residuo de la division entre dos numeros
    #En este caso, el residuo de la division entre el numero y 10
    suma = suma + (numero % 10)
    #El operador % devuelve el residuo de la division entre el numero y 10
    #Esto nos da el ultimo digito del numero
    numero = numero // 10

print(f"La suma de los digitos es: {suma}")
#El resultado es la suma de los digitos del numero ingresado.    