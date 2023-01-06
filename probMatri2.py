import numpy as  np
A=[[1,-1],[3,1]]
B=[[4,1],[-2,2]]

type(A)
A=np.matrix(A)
B=np.matrix(B)

print(A*B)