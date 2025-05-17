# EJERCICIOS PRÁCTICOS: PYTHON EN EL SECTOR AGROPECUARIO

# --- EJERCICIO 1: Registro de Parcelas y Cultivos ---
# Objetivo: Variables, tipos de datos, entrada/salida.

# print("--- Registro de Parcela Agrícola ---")
# id_parcela = input("Ingrese el ID de la parcela (ej: LOTE001): ")
# cultivo_actual = input("Ingrese el cultivo sembrado en la parcela (ej: Soja, Maíz, Girasol): ")
# hectareas_str = input(f"Ingrese la cantidad de hectáreas de la parcela {id_parcela}: ")
# fecha_siembra_str = input(f"Ingrese la fecha de siembra (DD/MM/AAAA) para {cultivo_actual}: ") # Formato string

# hectareas = float(hectareas_str) # Convertimos a flotante

# Calculamos una estimación de semillas necesarias (ejemplo: 80kg de semilla por hectárea para maíz)
# semillas_kg_por_hectarea = 0.0
# if cultivo_actual.lower() == "maíz":
#     semillas_kg_por_hectarea = 80.0
# elif cultivo_actual.lower() == "soja":
#     semillas_kg_por_hectarea = 90.0
# elif cultivo_actual.lower() == "girasol":
#     semillas_kg_por_hectarea = 5.0
# else:
#     print(f"No se especificó una tasa de siembra para {cultivo_actual}, se usará 0.")

# semillas_totales_necesarias = hectareas * semillas_kg_por_hectarea

# print("\n--- Resumen de la Parcela ---")
# print(f"ID Parcela: {id_parcela.upper()}")
# print(f"Cultivo: {cultivo_actual.title()}")
# print(f"Hectáreas: {hectareas} ha")
# print(f"Fecha de Siembra: {fecha_siembra_str}")
# if semillas_kg_por_hectarea > 0:
#     print(f"Semillas necesarias (aprox.): {semillas_totales_necesarias:.2f} kg")

# necesita_riego = cultivo_actual.lower() in ["maíz", "hortalizas"] # Maíz y hortalizas suelen necesitar más riego
# print(f"¿El cultivo '{cultivo_actual}' suele necesitar riego suplementario? {necesita_riego}")


# --- EJERCICIO 2: Inventario de Insumos Agrícolas (Listas y Tuplas) ---
# Objetivo: Manejo de colecciones para insumos.

# print("\n--- Inventario de Insumos ---")
# Lista de tuplas: (Nombre_Insumo, Cantidad_Disponible, Unidad, Proveedor_Principal)
# inventario_insumos = [
#     ("Fertilizante Triple 15", 5000.0, "kg", "Agroquímicos del Litoral"),
#     ("Semilla de Soja DM4800", 2500.0, "kg", "DonMario Semillas"),
#     ("Herbicida Glifosato", 800.0, "litros", "Agroservicios Chaco"),
#     ("Semilla de Maíz DK7270", 1200.0, "kg", "Dekalb")
# ]
# print("Inventario inicial:")
# for insumo in inventario_insumos:
#     print(f" - {insumo[0]} ({insumo[1]} {insumo[2]}) Proveedor: {insumo[3]}")

# Se realiza una compra de herbicida
# insumo_comprado_nombre = "Herbicida Glifosato"
# cantidad_comprada = 200.0 # litros

# for i, insumo in enumerate(inventario_insumos):
#     if insumo[0] == insumo_comprado_nombre:
#         # Las tuplas son inmutables, así que creamos una nueva tupla para actualizar
#         nueva_cantidad = insumo[1] + cantidad_comprada
#         inventario_insumos[i] = (insumo[0], nueva_cantidad, insumo[2], insumo[3])
#         print(f"\nActualización: {insumo_comprado_nombre} ahora tiene {nueva_cantidad} {insumo[2]}")
#         break
# print("\nInventario después de la compra:")
# for insumo in inventario_insumos:
#     print(f" - {insumo[0]} ({insumo[1]} {insumo[2]})")

# Se utiliza semilla de Maíz para la siembra del Ejercicio 1
# cultivo_sembrado_ej1 = "Maíz" # Supongamos que es maíz
# hectareas_ej1 = 50.0 # Supongamos 50 hectáreas
# semillas_por_ha_maiz = 80.0
# semilla_necesaria_ej1 = hectareas_ej1 * semillas_por_ha_maiz

# if cultivo_sembrado_ej1.lower() == "maíz":
#     for i, insumo in enumerate(inventario_insumos):
#         if "Semilla de Maíz" in insumo[0]: # Buscamos por parte del nombre
#             if insumo[1] >= semilla_necesaria_ej1:
#                 nueva_cantidad_semilla = insumo[1] - semilla_necesaria_ej1
#                 inventario_insumos[i] = (insumo[0], nueva_cantidad_semilla, insumo[2], insumo[3])
#                 print(f"\nSe utilizaron {semilla_necesaria_ej1} kg de {insumo[0]}. Stock restante: {nueva_cantidad_semilla} kg.")
#             else:
#                 print(f"\nAlerta: Stock insuficiente de {insumo[0]}. Necesarios: {semilla_necesaria_ej1} kg, Disponible: {insumo[1]} kg.")
#             break


# --- EJERCICIO 3: Identificación de Animales por Categoría (Comprensión de Listas) ---
# Objetivo: Clasificar animales de una tropa.

# print("\n--- Clasificación de Animales en Tropa ---")
# Lista de tuplas: (ID_Animal, Categoría, Peso_kg)
# Categorías: "Vaquillona", "Novillito", "Ternero", "Vaca"
# tropa_ganadera_lote_x = [
#     ("ANI001", "Vaquillona", 320), ("ANI002", "Novillito", 380), ("ANI003", "Ternero", 180),
#     ("ANI004", "Vaca", 450),       ("ANI005", "Vaquillona", 310), ("ANI006", "Novillito", 400),
#     ("ANI007", "Ternero", 195),    ("ANI008", "Vaquillona", 330), ("ANI009", "Vaca", 480)
# ]

# 1. Obtener una lista solo con los IDs de las Vaquillonas.
# ids_vaquillonas = [animal[0] for animal in tropa_ganadera_lote_x if animal[1] == "Vaquillona"]
# print(f"IDs de Vaquillonas en la tropa: {ids_vaquillonas}")

# 2. Obtener una lista de los pesos de todos los Novillitos.
# pesos_novillitos = [animal[2] for animal in tropa_ganadera_lote_x if animal[1] == "Novillito"]
# print(f"Pesos de Novillitos (kg): {pesos_novillitos}")
# if pesos_novillitos: # Calcular promedio solo si hay novillitos
#     promedio_peso_novillitos = sum(pesos_novillitos) / len(pesos_novillitos)
#     print(f"Peso promedio de Novillitos: {promedio_peso_novillitos:.2f} kg")

# 3. Crear una lista de tuplas (ID_Animal, "APTO FAENA") para animales que pesan más de 350 kg.
# animales_aptos_faena = [
#     (animal[0], "APTO FAENA") for animal in tropa_ganadera_lote_x if animal[2] > 350
# ]
# print(f"Animales aptos para faena (>350kg): {animales_aptos_faena}")

# 4. Contar cuántos terneros hay en la tropa.
# cantidad_terneros = len([animal for animal in tropa_ganadera_lote_x if animal[1] == "Ternero"])
# print(f"Cantidad de Terneros en la tropa: {cantidad_terneros}")


# --- EJERCICIO 4: Manejo de Plagas en Cultivos (Conjuntos) ---
# Objetivo: Usar conjuntos para identificar plagas comunes y específicas.

# print("\n--- Control de Plagas en Cultivos ---")
# Plagas comunes que afectan al Maíz
# plagas_maiz = {"Gusano cogollero", "Pulgón del maíz", "Chicharrita del maíz", "Oruga de la espiga"}

# Plagas comunes que afectan a la Soja
# plagas_soja = {"Chinche verde", "Oruga medidora", "Pulgón de la soja", "Arañuela roja"}

# Plagas detectadas en una inspección de campo esta semana
# plagas_detectadas_campo = {"Gusano cogollero", "Chinche verde", "Isoca bolillera", "Pulgón del maíz"}

# 1. ¿Qué plagas detectadas son comunes tanto al maíz como a la soja? (Esto no se puede hacer directamente con los conjuntos dados,
#    sino comparando las detectadas con cada uno de los conjuntos de plagas por cultivo)
# plagas_detectadas_en_maiz = plagas_detectadas_campo & plagas_maiz
# print(f"Plagas detectadas esta semana que afectan al Maíz: {plagas_detectadas_en_maiz}")

# plagas_detectadas_en_soja = plagas_detectadas_campo & plagas_soja
# print(f"Plagas detectadas esta semana que afectan a la Soja: {plagas_detectadas_en_soja}")

# 2. ¿Qué plagas de las detectadas son específicas del maíz (están en detectadas y en maíz, pero no en soja)?
# especificas_maiz_detectadas = (plagas_detectadas_campo & plagas_maiz) - plagas_soja
# print(f"Plagas detectadas esta semana, específicas del Maíz (y no comunes a la Soja): {especificas_maiz_detectadas}")

# 3. ¿Hay alguna plaga detectada que no sea común ni al maíz ni a la soja según nuestras listas? (Plaga nueva o no listada)
# plagas_conocidas_cultivos = plagas_maiz | plagas_soja # Unión de todas las plagas conocidas para estos dos cultivos
# plagas_nuevas_o_no_listadas = plagas_detectadas_campo - plagas_conocidas_cultivos
# print(f"Plagas detectadas esta semana que NO estaban en nuestras listas de Maíz o Soja: {plagas_nuevas_o_no_listadas}")

# 4. Si se aplica un insecticida que cubre "Gusano cogollero" y "Chinche verde", ¿qué plagas detectadas quedarían sin tratar?
# insecticida_cubre = {"Gusano cogollero", "Chinche verde"}
# plagas_sin_tratar = plagas_detectadas_campo - insecticida_cubre
# print(f"Plagas detectadas que quedarían sin tratar después del insecticida: {plagas_sin_tratar}")

# -------------------------------------------
# ¡Modifica los datos y prueba diferentes escenarios!