#SUMA DE MATRICES
a=[[21, 18, 35], [19, 11, 21],[12, 15, 20]]
b=[[11, 7, 21],[9, 15, 24],[23, 8, 12]]

def suma_matrices(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        m3=[]
        for i in range (len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j]+m2[i][j])
        return m3
    else:
        return None

def resta_matrices(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        m3=[]
        for i in range (len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j]-m2[i][j])
        return m3
    else:
        return None

def multiplicar_matrices(m1,m2):
    if len(m1[0])==len(m2):

        m3=[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)
        for i in range (len(m1)):
            for j in range(len(m2[0])):
                for k in range (len(m1[0])):
                    m3[i][j] += m1[i][k]*m2[k][j]
        return m3
    else:
        return None

c=suma_matrices(a,b)
d=resta_matrices(a,b)
e=multiplicar_matrices(a,b)

if c== None:
    print("No se puede sumar")
else:
    print("La suma de las matrices es: ")
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")

if d== None:
    print("No se puede restar")
else:
    print("La resta de las matrices es: ")
    for fila in d:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")

if e== None:
    print("No se puede multiplicar")
else:
    print("La multiplicacion de las matrices es: ")
    for fila in e:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")