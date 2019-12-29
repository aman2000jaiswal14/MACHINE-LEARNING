import numpy as np
zr = np.zeros([3,4]) # gives an array of shape 3,4 with 0.0(float)
print("Zero filed array zr = \n",zr)

ar = np.ones([4,4])
print("1's filed array ar = \n",ar)

tr = np.ones([31,31])*2     # also from +1
print("2's filed array tr",tr)

print(ar.dtype)

# We can create numpy array from range
ar = np.arange(1,6)    # create 1,2,3,4,5 an array excluding 6
print("ar = ", ar )  # [1,2,3,4,5]

ar[3] = 16
print("After updating, ar = ",ar)