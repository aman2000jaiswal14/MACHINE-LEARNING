# cross validation regression MAE
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

filename = 'housing.csv'

hnames = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
          'RAD','TAX','PTRATIO','B','LSTAT','MEDV']

dataframe = read_csv(filename,names = hnames)
array = dataframe.values

X = array[:,0:13]
Y = array[:,13]

kfold = KFold(n_splits=10)
model= LinearRegression()

scoringMethod = 'neg_mean_absolute_error'   # MAE(MEAN ABSOLUTE ERROR)
results = cross_val_score(model,X,Y,
                          cv = kfold, scoring= scoringMethod)
print("MAE: %.3f (%.3f)"%(results.mean(),results.std()))
