# Assignment
import numpy
filename= 'indians-diabetes.data.csv'
raw_data=open(filename,'r')
data=numpy.loadtxt(raw_data,delimiter=",")
print("Numpy loadtxt: ",data.shape)
raw_data.close()
print("Sum column ", data.sum(axis=0))
print("Sum row",data.sum(axis=1))
