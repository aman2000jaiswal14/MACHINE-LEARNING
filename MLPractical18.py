import numpy as np
n4 = np.array([10,-1,0,90,300,3,-6,2])
n3 = np.array([777,555,222,111,999,666])
print("n3  =      : " , n3)
print("n3.argsort() : ",n3.argsort())  # gives the index of sorted array  [3 2 1 5 0 4]
print("n3  =     :",n3) # extern sort
indexarr = n3.argsort()
print("max",n3[indexarr[-1]])
print("min",n3[indexarr[0]])
print("3 smaller value",n3[indexarr[0:3]])

# Trick 1 : to print the array in sorted order
for i in n3.argsort():
    print(n3[i],end=" ")

# Trick 2: To print the array in sorted order
print(n3[n3.argsort()])
print("n3 = ",n3)