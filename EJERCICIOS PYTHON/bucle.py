from os import system

control = True

while control == True:
    print("1. Calcular primo\n2. Factorial\n3. Salir")
    opcion = int(input("Ingrese la opción: "))
    if opcion == 1:
        system("cls")
        numero = int(input("Ingrese el número a probar"))
        cont = 0
        for divisor in range(1,numero+1):
            if (numero % divisor) == 0:
                cont += 1
        if cont > 2:
            print(f"{numero} no es primo")
        else:
            print(f"{numero} es primo")
    elif opcion == 2:
        system("cls")
        numero = int(input("Ingrese la opción: "))
        fact = 1
        for i in range(1, numero+1):
            fact *= i
        print(f"{numero}={fact}")
    elif opcion == 3:
        control = False
    else:
        print("Opción no válida. Intente nuevamente.")
        opcion = int(input("Ingrese la opción: "))
