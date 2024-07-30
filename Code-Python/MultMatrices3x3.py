import numpy as np

print ('')
print ('Multiplicacion de matrices 3x3, AB')
A=np.array([[-1,2,3],[-3,4,1],[4,-1,3]])
B=np.array([[-2,3,1],[1,3,-3],[-5,0,2]])
I=A.dot(B)
print (I)

