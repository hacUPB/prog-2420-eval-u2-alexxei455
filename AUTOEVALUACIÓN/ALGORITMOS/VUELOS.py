import random
import datetime

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

hoy = datetime.datetime.now()
print(hoy)
# Lista de días válidos de la semana
fecha = input("Ingerese la fecha del viaje con formato dd/mm/aaaa: ")
fecha_sis = datetime.datetime.strptime(fecha, "%d/%m/%Y")
print(fecha_sis)

dia = fecha_sis.weekday()

print(dia)

print(dias_validos_semana[dia])


# Calcular el precio del billete
if distancia < 400:
    if dias_validos_semana in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 79900
    else:
        precio = 119900
else:
    if dias_validos_semana in ["lunes", "martes", "miércoles", "jueves"]:
        precio = 156900
    else:
        precio = 213000

# Mostrar el precio calculado
print(f"\nEl vuelo de {origen} a {destino} el día {fecha_sis.day} del mes {fecha_sis.month} del {fecha_sis.year}, tendrá un costo de ${precio}.\n")

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
print(f"{titulo}{nombre} se le ha asignado el asiento {numero_asiento}{asiento} para el vuelo del {fecha_sis.day} del mes {fecha_sis.month} del {fecha_sis.year} con origen {origen} y destino {destino}.")


