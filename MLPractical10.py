a=10
print(type(a))

a=12.5
print(type(a))

import numpy as np
nparr = np.array( [1,2,3])

print(type(nparr))
print( "nparr.dtype=", nparr.dtype) # gives datatype of inner element of nparr

a=7
b=2
print(a/b)
print("nparr.shape = ",nparr.shape)  # return array
print("nparr.size = ",nparr.size)    # return int