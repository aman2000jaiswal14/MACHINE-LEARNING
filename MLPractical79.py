import pandas as pd
import numpy as np

s= pd.Series ([1,3,np.nan,15,7,8])
print(s)
d=pd.Series([1,3,4,15,7,8])
print(d)

#dates=pd.date_range( '20190101',peroids=6,freq="D")
#print(dates) # It contains 6 dates as array
#print(dates[0])
#print(np.random.randn(6,4))
df=pd.DataFrame(np.random.randn(6,4),
                index=[0,1,2,3,4,5],
                columns=['A','B','C','D'])

print("Heading in Dataframe:",df.columns)
print("Row Headings",df.index)
print("Values in Dataframe:",df.values)

df['E']= df['A'].apply(lambda x: 1 if(x>0)else 0)  #FEATURE ENGINEERING IN TERM OF MACHINE LEARNING
print(df)
df['F']=df['B'].apply(lambda x: 10 if(x>2) else 0 )
print(df)

print(df.dtypes)
print(df.head())
print(df.tail(2))  #FOR LAST TWO
print(df.sample(3))#IT WILL CHOOSE RANDOMLY
print(df.describe())
#              A         B         C         D         E          F
#count  6.000000  6.000000  6.000000  6.000000  6.000000   6.000000
#mean   0.184210  1.502436  0.606941 -0.421703  0.666667   1.666667
#std    1.339966  1.026611  1.338216  0.980841  0.516398   4.082483
#min   -1.230049  0.111637 -2.061939 -1.345348  0.000000   0.000000
#25%   -0.855640  0.929290  0.747342 -1.096234  0.250000   0.000000
#50%    0.175328  1.614954  1.138135 -0.760808  1.000000   0.000000
#75%    0.675131  1.801646  1.270081  0.069350  1.000000   0.000000
#max    2.342218  3.108459  1.496174  1.198721  1.000000  10.000000

print(df.describe(include="all"))  #FOR ALL TYPE OF DATA INCLUDING OBJECT TYPE ALSO

print("original values:\n",df)

print("Sorted values:\n")
print(df.sort_values(by='B',ascending=True))