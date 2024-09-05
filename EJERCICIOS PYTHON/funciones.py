#1. Función que recibe cantidad de datos float, rango de valores y retorna una lista
#2. unción que recibe una lista y calcula el promedio y la desviación estandar
#3. Función que calcula cuantos datos están por encima del promedio en una lista y cuales son esos datos

#1.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from random import uniform
from math import sqrt
def crea_lista_float(cantidad:int, lim_infe:float, lim_supe:float):
    #1. Crea una lista vacia
    aleatorios_float =[]
    #2. Utilizo un bucle
    for i in range(cantidad):
        #3. Genero el número aleatorio
        numero = uniform(lim_infe, lim_supe)
        #4. Agrego el número a la lista
        aleatorios_float.append(numero)
    return aleatorios_float

def estadisticas(datos:list):
    promedio = sum(datos) / len(datos)
    #Calculamos la desviación estandar
    suma = 0
    for xi in datos:
        suma += (xi - promedio) ** 2
    termino = suma / len(datos)
    desv = sqrt(termino)
    return promedio, desv

def sobre_promedio(list:list, promedio:float):
    #Calculamos cuantos datos están por encima del promedio
    contador = 0
    mayores = []
    for xi in list:
        if xi > promedio:
            contador += 1
            mayores.append(xi)
    return
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Programa principal
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print("Ejemplo de uso de funciones")

lista_aleatorios = crea_lista_float(100, 10.0, 20.0)
print(lista_aleatorios)

prom, desv = estadisticas(lista_aleatorios)
print(f"Promedio = {prom}, Desviación estandar = {desv}")

datos_sobre_promedio = sobre_promedio(lista_aleatorios, prom)
print(f"Hay {sobre_promedio} datos sobre el promedio")



#2.


