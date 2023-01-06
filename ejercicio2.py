A = [20, 15, 12, 11, 8, 4, 1]

maxi = 20
mini = maxi 

for i in A:
    if i < mini:
        mini = i
print(f'El minimo del array es: {mini}')

A.remove(mini)

suma = 0
for j in A:
    suma += j

print(f'Promedio sin la nota mas baja {suma / len(A)}')