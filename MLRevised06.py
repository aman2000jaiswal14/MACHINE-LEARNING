import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings(action="ignore")
def linear_model_main(X,Y,quest):
    regr = LinearRegression()
    regr.fit(X,Y)
    ans = regr.predict([quest])
    predictions = {}
    predictions['coefficient']=regr.coef_
    predictions['intercept'] = regr.intercept_
    predictions['ans']= ans
    plt.scatter(X,Y,c='g')
    predicted_y = regr.predict(X)
    plt.scatter(X,predicted_y,c='r')
    plt.plot(X,predicted_y,'r-')
    plt.scatter(quest,ans,c='b')
    plt.show()
    return predictions


if __name__ == '__main__':
    filename = 'mydata3.csv'
    df = pd.read_csv(filename)
    X1=[]
    X2=[]
    Y = []
    for x1,x2,y in zip(df['x1'],df['x2'],df['y']):
        X1.append([float(x1)])
        X2.append([float(x2)])
        Y.append(float(y))
    quest1 = [1]
    quest2=[3]
    result1= linear_model_main(X1,Y,quest1)
    print("answer  1:  ",result1['ans'])
    print("intercept 1 : ",result1['intercept'])
    print("coefficent 1: ", result1['coefficient'])
    result2 = linear_model_main(X2, Y, quest2)
    print()
    print("answer  2:  ", result2['ans'])
    print("intercept 2 : ", result2['intercept'])
    print("coefficent 2: ", result2['coefficient'])
    m=result1['ans']+result2['ans']
    print("mean ans = ",m/2)
