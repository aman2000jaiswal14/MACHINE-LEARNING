import numpy as np
n1 = np.array([4,5,6])
n2 = np.array([1,2,3])

print("\n\n")
print("n1  =  ",n1)
print("n2  =  ",n2)
print("n1 + n2 = ",n1 + n2)
print("n1 - n2 = ",n1 - n2)
n3= np.array([4,5,6,7])
print(n1+n3)      # gives error (ValueError: operands could not be broadcast together with shapes (3,) (4,)
