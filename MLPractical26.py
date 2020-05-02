import numpy as np
x  = np.array([1,2,3,2,1])

m_x = np.mean(x)                      # external method if we need new array mean

print("Mean of x =", m_x)
print("x.mean() = ",x.mean() )         # internal method if we need to use same array to store mean
print("np.median(x) =",np.median(x))   # median has only external function (not have internal function)
print("x.std() = ",x.std())

