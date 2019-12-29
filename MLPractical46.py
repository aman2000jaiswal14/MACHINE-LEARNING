import matplotlib.pyplot as plt
import numpy as np

# Use numpy to generate bunch of random data in
n= 5 + np.random.randn(1000)
print("n= ",n)
# m= [m for m in range(len(n))]

m= list( range(len(n)))
print("m = ",m)

plt.bar(m,n)
plt.title("Raw Data")
plt.show()

plt.hist(n,bins=10) # bin form bucket of data
plt.title("Histogram")
plt.show()