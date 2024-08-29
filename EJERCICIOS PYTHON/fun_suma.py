Lista = [4,56, 66, 77, 32, 11, 12, 34, 34, 56, 7, 5, 3, 6, 77]

acum = 0
n_elem = len(Lista)
cont = 0
while cont < n_elem:
    acum += Lista[cont]
    cont += 1
print(f"La suma es {acum} y debe dar {sum(Lista)}")
