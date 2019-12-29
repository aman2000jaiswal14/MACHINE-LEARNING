# Basic reduction
# ---------------
# computing sums

import numpy as np
x = np.array([1,2,3,4])

print("np.sum(x) : ",np.sum(x))         # 10  external addition  for old version of array x specially
print("x.sum():",x.sum())               # 10  internal addition

print("---Sum by rows and by columns:---")

x = np.array([[1,2],[3,4]])
print("x = \n", x )

print(x.sum())

print(x.sum(axis=0))   # columns ( first dimension
# array([4,6])
print(x[:,0].sum() , x[:,1].sum() )
# 4 , 6
print(x[0,:].sum(),x[1,:].sum())

print(x.sum(axis=1))
