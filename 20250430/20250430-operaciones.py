import math

# Operaciones básicas en Python

# Suma
def suma(a, b):
    return a + b

# Resta
def resta(a, b):
    return a - b

# Multiplicación
def multiplicacion(a, b):
    return a * b

# División
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

# División entera
def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: División por cero"

# Módulo (resto de la división)
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: División por cero"

# Potencia
def potencia(a, b):
    return a ** b

# Operaciones avanzadas usando la biblioteca math

# Raíz cuadrada
def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Raíz cuadrada de un número negativo"

# Logaritmo natural
def logaritmo_natural(a):
    if a > 0:
        return math.log(a)
    else:
        return "Error: Logaritmo de un número no positivo"

# Logaritmo en base 10
def logaritmo_base10(a):
    if a > 0:
        return math.log10(a)
    else:
        return "Error: Logaritmo de un número no positivo"

# Factorial
def factorial(a):
    if a >= 0 and isinstance(a, int):
        return math.factorial(a)
    else:
        return "Error: Factorial de un número negativo o no entero"

# Ejemplo de uso
if __name__ == "__main__":
    print("Suma: ", suma(5, 3))
    print("Resta: ", resta(5, 3))
    print("Multiplicación: ", multiplicacion(5, 3))
    print("División: ", division(5, 3))
    print("División entera: ", division_entera(5, 3))
    print("Módulo: ", modulo(5, 3))
    print("Potencia: ", potencia(5, 3))
    print("Raíz cuadrada: ", raiz_cuadrada(25))
    print("Logaritmo natural: ", logaritmo_natural(10))
    print("Logaritmo base 10: ", logaritmo_base10(10))
    print("Factorial: ", factorial(5))