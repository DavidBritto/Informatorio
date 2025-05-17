anio_actual = 2025
mayoria_edad = 18

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))

anio_usuario = anio_actual - anio_nacimiento
if (anio_usuario >= mayoria_edad):
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")