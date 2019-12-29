import numpy as np

na = np.array( [ [1,2,3],
                 [4,5,6] ] )

print("na = \n",na)
print("na.transpose() = \n",na.transpose())
print("na = \n",na)

print("np.eye = \n",np.eye(6)) # To create an identity matrix of order 6

a=np.ones([3,3])
a=a*3          # operation broadcasting
a[2,2]=4
I = np.eye(3)    # I stands for Identity matrix some author write it as I
b = np.dot(a,I)  # dot is matrix multiplication
print(a)
print()
print(I)
print()
print(b)

nb =np.array([[1,2],
             [5,6]])
print("np.dot(nb,nb)= \n",np.dot(nb,nb))