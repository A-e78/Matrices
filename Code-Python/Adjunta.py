import numpy as np
from numpy import size
from numpy import zeros
from numpy import matrix

#La matriz original
A=matrix([[1,2,-1],[0,1,2],[5,1,1]])
#Se vacia la matriz de cofaactores
Acof=matrix(zeros((3,3)))
#Se eligen las entradas de la matriz
aij=matrix(range(3))
print ('Orden de los elementos, aij\n',aij)
print ('Se vacia la matriz Acof\n',Acof)

for i in range (size(A,0)):
  for j in range (size(A,1)):
     factij=aij[aij!=i]
     Mij=aij[aij != j]
     B=A[[[factij[0,0]],[factij[0,1]]],Mij]
     detA=np.linalg.det(B)
     Acof[i,j]=detA*np.power(-1,i+j)

print ('')
print ('Matriz Original A\n', A)
print ('')
print ('Matriz Adjunta \n', Acof)
print ('')
