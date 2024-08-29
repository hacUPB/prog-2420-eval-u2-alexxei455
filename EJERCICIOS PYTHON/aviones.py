aviones = ["F4 PHANTOM II" , "F5 TIGER" , "F8 CRUSADER" , "F14 TOMCAT", "F15 EAGLE" , "F16 FIGHTING FALCON" , "F18 HORNET" , "F22 RAPTOR" , "F35 LIGHTING II"]
cont = 1
for avion in aviones:
    print(f"Avión {cont} --> {avion}")
    cont = cont + 1

    indice = 0
    cont = len(aviones)
    while indice < cont:
        print(f"Avión {indice+1} --> {aviones[indice]}")
        indice = indice + 1
        
for i in range(10):
    print("SEXOOOOOOOOOOO")