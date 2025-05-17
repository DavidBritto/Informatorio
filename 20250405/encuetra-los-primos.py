# Ejercicio: Definir una lista del 1 al 1000 y determinen todos los numeros primos que aparecen
# entre el 1 y el 1000, y guardarlos en una lista llamada numeros_primos.

# Resolucion:
numeros_primos = [] # Inicializa una lista vacía para almacenar los números primos.

# Itera sobre los números del 1 al 1000 (incluyendo el 1000).

for numero_actual in range(2, 1001):
    # Asume que el número actual es primo.
    es_este_numero_primo = True 

    for posible_divisor in range(2, numero_actual):
        # Si el número actual es divisible por el posible divisor, no es primo.
        if numero_actual % posible_divisor == 0:
            # Cambia la variable a False si se encuentra un divisor.
            es_este_numero_primo = False
            break # Sale del bucle si se encuentra un divisor.
    # Si el número actual es primo, se agrega a la lista.
    if es_este_numero_primo:
        numeros_primos.append(numero_actual) # Agrega el número primo a la lista.

print ("Los números primos entre 1 y 1000 son: ", numeros_primos) 

#Me pongo creativo y le agrego un contador de primos
print(f"\nTotal de números primos encontrados: {len(numeros_primos)}")