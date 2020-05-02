import numpy as np
a=np.random.randint(10,size=5) # by default start value with 0 if not mentioned
print(a)
print(type(a))
b=np.random.randint(-10,10,size=5)  # ending value is always greater than starting value other wise give error
#error is value error (low>=high)
print(b)
