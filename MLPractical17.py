import numpy as np
n4 = np.array([10,-1,0,90,300,3,-6,2])
print("Before : ", n4)
print(sorted(n4))  # extern sorted (original array is not distrubed , new array is used to sort )
print("After : ",n4)
n4.sort() # In-place sorting    (internal sort) use same array to sort
print("After n4.sort() = ",n4)
# None  is a keyword of python similar to Null in c
# None True and False represent a value( not action), thus they start from upercase
# None is None type datatype
