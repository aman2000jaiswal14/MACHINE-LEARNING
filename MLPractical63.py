# Normalize data
from sklearn.preprocessing import Normalizer
from pandas import read_csv

filename='indians-diabetes.data.csv'
names= ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe= read_csv(filename,names=names)
array= dataframe.values

# separate array into input and output components
X = array[:,0:8]
Y = array[:,8]
scaler = Normalizer()
normalizedX = scaler.fit_transform(X)

print(normalizedX[:30,:])
