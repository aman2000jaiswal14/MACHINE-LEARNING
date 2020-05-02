import numpy as np
print("--Element wise comparisons:--")

a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print("a == b : ",a==b)
print(" a > b : ", a>b )

print( "---Array wise comparisions:---")
a=np.array([1,2,3,4])
b=np.array([4,2,2,4])
c=np.array([1,2,3,4])
print("np.array_equal(a,b):",np.array_equal(a,b))   # False
print("np.array_equal(a,c):",np.array_equal(a,c))   #True

print("----Logical operation:----")
a = np.array([1,1,0,0], dtype=bool)
b = np.array([1,0,1,0], dtype=bool)
print("a= ",a)
print("b= ",b)
print(np.logical_or(a,b))
print(np.logical_and(a,b))

