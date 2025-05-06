# Programa que determina el mes a partir de una fecha en formato ISO
# y vuelve a pedir la fecha si el mes es inválido o el formato es incorrecto.

while True:  # Inicia un bucle que se repetirá hasta que se rompa con 'break'
    # Solicitar al usuario una fecha en formato ISO (YYYYMMDD)
    fecha_iso = input("Introduce una fecha en formato ISO (YYYYMMDD): ")

    # Validación básica de formato y longitud
    if len(fecha_iso) == 8 and fecha_iso.isdigit():
        # Extraer la parte del mes como string y luego convertirla a entero
        mes_str = fecha_iso[4:6]
        mes = int(mes_str)

        nombre_mes = "" # Variable para guardar el nombre del mes20

        # Determinar el nombre del mes usando estructuras de control
        if mes == 1:
            nombre_mes = "Enero"
        elif mes == 2:
            nombre_mes = "Febrero"
        elif mes == 3:
            nombre_mes = "Marzo"
        elif mes == 4:
            nombre_mes = "Abril"
        elif mes == 5:
            nombre_mes = "Mayo"
        elif mes == 6:
            nombre_mes = "Junio"
        elif mes == 7:
            nombre_mes = "Julio"
        elif mes == 8:
            nombre_mes = "Agosto"
        elif mes == 9:
            nombre_mes = "Septiembre"
        elif mes == 10:
            nombre_mes = "Octubre"
        elif mes == 11:
            nombre_mes = "Noviembre"
        elif mes == 12:
            nombre_mes = "Diciembre"
        # No hay 'else' aquí para 'nombre_mes' si mes no es 1-12; permanecerá vacío.

        if nombre_mes:  # Si 'nombre_mes' tiene un valor (es decir, el mes fue válido 1-12)
            # Mostrar el resultado al usuario
            print(f"El mes introducido es: {nombre_mes}")
            break  # Salir del bucle 'while' porque la entrada fue válida y procesada
        else: # Si 'nombre_mes' está vacío, significa que el número de mes (1-12) fue inválido
            print("El número de mes extraído de la fecha es inválido (ej. 01 para Enero, 12 para Diciembre). Intenta de nuevo.")
            # El bucle continuará
    else:
        print("Formato de fecha incorrecto. Debe ser YYYYMMDD (8 dígitos numéricos). Intenta de nuevo.")
        # El bucle continuará

# El programa solo llega aquí después de un 'break'
print("Proceso finalizado.")