# Rescale data (custome range between 1 and 5)
import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

filename = 'indians-diabetes.data.csv'
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pd.read_csv(filename,names=hnames)

array = dataframe.values  # give the dataframe without metadata

# separate array into input and output components
X = array[ : , 0 : 8 ] # [row,cols]
Y = array[ : , 8 ]
scaler = MinMaxScaler(feature_range=(1,5))  # rearrange the scale in 1 to 5

# First Method
rescaledX = scaler.fit_transform(X)
# summarize transformed data
set_printoptions(precision= 2)
print( rescaledX [ : 30 ,: ] ) # [row,cols]
