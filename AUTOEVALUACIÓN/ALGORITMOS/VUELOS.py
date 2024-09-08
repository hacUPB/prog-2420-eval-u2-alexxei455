import random

# 1. Información del Usuario
titulo = input("Ingrese su título (Sr. o Sra.): ")
nombre = input("Ingrese su nombre completo: ")

# Saludo personalizado
print(f"{titulo} {nombre}, ¡Bienvenido a FastFast Airlines!\n")

# 2. Selección de Vuelo
# Lista de ciudades válidas
ciudades_validas = ["Medellín", "Bogotá", "Cartagena"]

# Validación para la ciudad de origen
while True:
    origen = input("Ingrese la ciudad de origen (Medellín, Bogotá, Cartagena): ").capitalize()
    if origen not in ciudades_validas:
        print("Error: Ciudad de origen no válida. Por favor ingrese una de las ciudades válidas (Medellín, Bogotá, Cartagena).")
    else:
        break  # Sale del bucle si la ciudad de origen es válida

# Validación para la ciudad de destino
while True:
    destino = input("Ingrese la ciudad de destino (Medellín, Bogotá, Cartagena): ").capitalize()
    if destino not in ciudades_validas:
        print("Error: Ciudad de destino no válida. Por favor ingrese una de las ciudades válidas (Medellín, Bogotá, Cartagena).")
    else:
        break  # Sale del bucle si la ciudad de destino es válida

# Verificar distancia entre las ciudades
if (origen == "Medellín" and destino == "Bogotá") or (origen == "Bogotá" and destino == "Medellín"):
    distancia = 240
elif (origen == "Medellín" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Medellín"):
    distancia = 461
elif (origen == "Bogotá" and destino == "Cartagena") or (origen == "Cartagena" and destino == "Bogotá"):
    distancia = 657
else:
    print("Error: Las ciudades seleccionadas no son válidas.")
    exit()


# Lista de días válidos de la semana
dias_validos_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

# Validación para el día de la semana
while True:
    dia_semana = input("Ingrese el día de la semana: ").lower()
    if dia_semana not in dias_validos_semana:
        print("Error: Día de la semana no válido. Por favor ingrese un día válido (lunes a domingo).")
    else:
        break  # Sale del bucle si el día es válido

# Validación para el día del mes (1-30)
##Video de try-except: https://www.youtube.com/watch?v=IFfdRY609Fg&ab_channel=UskoKruM2010
while True:
    try:
        dia_mes = int(input("Ingrese el día del mes (1-30): "))
        if dia_mes < 1 or dia_mes > 30:
            print("Error: Día del mes fuera de rango. Por favor ingrese un número entre 1 y 30.")
        else:
            break  # Sale del bucle si el día es válido
    except:
        print("Error: Por favor ingrese un número entero válido.")


# Calcular el precio del billete
if distancia < 400:
    if dia_semana in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 79900
    else:
        precio = 119900
else:
    if dia_semana in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 156900
    else:
        precio = 213000

# Mostrar el precio calculado
print(f"\nEl vuelo de {origen} a {destino} el día {dia_semana}, {dia_mes} tendrá un costo de ${precio}.\n")

# 3. Asignación de Asiento
preferencia_asiento = input("¿Prefiere asiento en pasillo, ventana o sin preferencia? ").lower()

if preferencia_asiento == "pasillo":
    asiento = "C"
elif preferencia_asiento == "ventana":
    asiento = "A"
else:
    asiento = "B"

# Asignar un número de asiento aleatorio
numero_asiento = random.randint(1, 29)

# Mostrar el asiento asignado
print(f"{titulo}{nombre} se le ha asignado el asiento {numero_asiento}{asiento} para el vuelo del {dia_semana} {dia_mes} con origen {origen} y destino {destino}.")


