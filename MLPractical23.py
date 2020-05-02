import numpy as np
print("--Transcendental functions:---")
a = np.arange(0,6)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))

# Shape mismatches : Error
a = np.arange(4)
# print( a + np.array([1, 2]))  # Error
