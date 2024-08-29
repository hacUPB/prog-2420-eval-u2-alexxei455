# Menú de operaciones básicas
print ("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nT. Residuo")
opcion = input("Ingrese la opción deseada:")
if opcion != "S" or "s" or "R" or "r" or "M" or "m" or "D" or "d" or "T" or "t":
    print("Opción no válida...!")
else:
    numero1 = float(input("Ingrese el primer valor: "))
    numero2 = float(input("Ingrese el segundo valor: "))

    if opcion == "S" or opcion == "s":
        resultado = numero1 + numero2
    elif opcion == "R" or opcion == "r":
        resultado = numero1 - numero2
    elif opcion == "M" or opcion == "m":
        resultado = numero1 * numero2
    elif opcion == "D" or opcion == "d":
        resultado = numero1 / numero2
    elif opcion == "T" or opcion == "t":
        resultado = numero1 % numero2
    else:
        print("Opción no valida...!")
    print (f"Elresultado es: {resultado}")

