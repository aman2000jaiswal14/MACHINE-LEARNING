import numpy as np
import matplotlib.pyplot as plt
filename= 'indians-diabetes.data.csv'
raw_data = open(filename,'r')
data=np.loadtxt(raw_data,delimiter=",")
raw_data.close()
print(data)
plt.plot(data[:,0],data[:,8],'rd',label='dot1');
plt.plot(data[:,2],data[:,8],'bo',label='dot2')
plt.legend(loc="best")
plt.show()
plt.plot(data[:,3],data[:,7],'go',label='skin vs age')
plt.legend(loc="best")
plt.show()
plt.plot(data[:,7],data[:,3],'go',label='age vs skin')
plt.legend(loc = 'best')
plt.show()

