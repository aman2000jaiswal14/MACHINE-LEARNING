import numpy as np
a = np.array([1,2,3,4])
print("a + 1 =", a+1)
print("a = ",a)
print("a**2 = ",a**2)  # scalar broadcasting

# All arithmetic operates elementwise:
a = np.array([1,2,3,4])
b = np.ones(4) + 1
print( a )
print( b )
print( "a - b : ", a - b)
print( " a * b : ", a * b)
print("49**.5 = ",49**.5)  # exponent operator to calculate square root

print("ar **.5 = \n",(np.arange(101,111))**.5) # print sqroot of 101 to 110

j = np.arange(5)
print(2**(j+1)-j)
