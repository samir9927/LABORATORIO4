matriz=[[1,2,3],
        [4,5,6]]

def transponer(m):
    t=[]
    for i in range (len(m[0])):
        t.append([])
        for j in range(len((m))):
            t[i].append(m[j][i])
    return t

transpuesta=transponer(matriz)

for linea in matriz:
    for elemento in linea:
        print(elemento, end="")
    print()

print("------------------")

for linea in transpuesta:
    for elemento in linea:
        print(elemento, end=" ")
    print()