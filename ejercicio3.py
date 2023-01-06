tamaño = int(input("Ingresa el tamaño del vector "))
multiplos = int(input("Ingresa el número de multiplos "))
array = []

for i in range(0, tamaño):
    array.append(i * multiplos)

print(array)