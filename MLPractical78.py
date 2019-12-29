import warnings

warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]

kfold = KFold(n_splits=10)

# 1) Spot cheching for Logistic Regression
# ----------------------------------------
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold, )
print("validation Score for LogisticdRegression: ", results.mean())

# 2) Spot checking for Linear Discriminant Analysis(LDA)
# -------------------------------------------------------
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

model = LinearDiscriminantAnalysis()
results = cross_val_score(model, X, Y, cv=kfold)
print("valdiation score for Linear Discriminant Analysis : ", results.mean())

# 3) Spot checking for k-Nearest Neighbors(kNN)
# -------------------------------------------------------------------
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print("validation score for kNN : ", results.mean())

# 4) Spot checking for Guassian Naive Bayes
# ---------------------------------------------------------------

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for GaussianNB : ", results.mean())

# spot checking for classification and regression trees
# (cart or just decision tree)
# ---------------------------------------------------

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print("validation score for cart decision tree : ", results.mean())

# spot ckecking for support vector machines(svm)
# ---------------------------------------------------
# svm seek a line that best separates two classes.
# those data instances that are closest to the line that
# best seprates the classes are called support vectors
# and influence where the if line is placed

from sklearn.svm import SVC

model = SVC()
results = cross_val_score(model, X, Y, cv=kfold)
print("validation score for SVM : ", results.mean())
