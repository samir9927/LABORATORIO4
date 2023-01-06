tamaño = int(input("Ingrese el tamaño del vector : "))
array1 = []
array2 = []

for i in range(tamaño):
    array1.append(input("Ingresa un nombre: "))

print(array1)

for x in range(tamaño): 
    array2.append(len(array1[x]))

print(array2)