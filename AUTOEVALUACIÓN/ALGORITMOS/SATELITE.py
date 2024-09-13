import time

def obtener_float_valido(mensaje, minimo=0, es_positivo=True):
    """Solicita un valor flotante al usuario y valida que sea un número válido."""
    while True:
        #Video de try-except: https://www.youtube.com/watch?v=IFfdRY609Fg&ab_channel=UskoKruM2010
        try:
            valor = float(input(mensaje))
            if es_positivo and valor < minimo:
                print(f"Por favor, ingrese un valor mayor que {minimo}.")
            else:
                return valor
        except:
            print("Entrada no válida. Por favor, ingrese un número.")

def calcular_orbitas(altitud, altitud_minima, cd):
    """Simula el descenso del satélite y cuenta las órbitas."""
    altitud_perdida = 0
    orbitas = 0

    while altitud > altitud_minima and cd > 0:
        altitud_perdida = altitud * cd
        altitud -= altitud_perdida
        orbitas += 1
        cd += 0.0001

        print(f"En la órbita #{orbitas}, la altitud del satélite es: {altitud:.2f} km")
        time.sleep(0.25)  # Simula el tiempo entre órbitas

    return orbitas, altitud

def main():
    # Obtener datos del usuario con validación
    altitud = obtener_float_valido("Ingrese la altitud inicial del satélite (en km): ", 0)
    altitud_minima = obtener_float_valido("Ingrese la altitud mínima de seguridad (en km): ", 0)
    cd = obtener_float_valido("Ingrese el coeficiente de arrastre inicial (valor positivo): ", 0, es_positivo=True)

    if cd < 0.00001:
        print("Satélite estable.")
        return

    # Simular el descenso del satélite
    orbitas, altitud_final = calcular_orbitas(altitud, altitud_minima, cd)

    # Comprobar si el satélite reingresó en la atmósfera
    if altitud_final < altitud_minima:
        print(f"Se ha perdido conexión con el satélite después de {orbitas} órbitas.")
    else:
        print(f"El satélite se ha estabilizado después de {orbitas} órbitas.")

if __name__ == "__main__":
    main()
