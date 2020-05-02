import numpy as np
print("-------------------------------------")
ddarr=np.array([[1,2,3],[4,5,6]])


print("ddarr.ndim = ", ddarr.ndim) # gives no. of dimension but the pattern should be symmetric

print("ddarr.shape = ",ddarr.shape)
# ddarr.shape = (2L, 3L)

print("ddarr.size = ", ddarr.size )
print("len(ddarr) = ", len(ddarr))
print("ddarr.dtype = ",ddarr.dtype)
print(ddarr)

print("*******************************")
print("ddarr[0,1] = ",ddarr[0,1])
print("ddarr[0] = " , ddarr[0])

print("ddarr[ : , 0]=",ddarr[ : , 0 ])  # [ : ,0] it says from  : (beg to end ) of row print 0th column
print("ddarr[1, :]=", ddarr[1 , :])     # [1, ] no error but |v
print("ddarr[ : ,2]=",ddarr[ : ,2])     # [ , 2] gives error
