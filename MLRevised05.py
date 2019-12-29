import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from sklearn.linear_model import LinearRegression
def linear_model(x,y,q):
    regr = LinearRegression()
    regr.fit(x,y)
    ans= regr.predict([q])
    predicted = {}
    predicted['ans'] =ans
    predicted['intercept'] = regr.intercept_
    predicted['coefficient']=regr.coef_
    z1=[]
    z2=[]
    for i in x:
        z1.append(i[0])
        z2.append(i[1])
    all_predicted_y = regr.predict(x)
    fig = plt.figure()
    ax = fig.add_subplot(111,projection = '3d')
    ax.scatter(z1,z2,y,c= 'r')
    ax.scatter(z1,z2,all_predicted_y,c='g')
    ax.scatter(q[0],q[1],ans,c = 'b')
    ax.plot(z1,z2,all_predicted_y,c='g')
    plt.tight_layout()
    plt.show()
    return predicted
if __name__ == '__main__':
    filename = 'mydata3.csv'
    df = pd.read_csv(filename)
    X=[]
    Y = []
    for x1,x2,y in zip(df['x1'],df['x2'],df['y']):
        X.append([float(x1),float(x2)])
        Y.append(float(y))
    quest = [9,2]
    result= linear_model(X,Y,quest)
    print("answer  :  ",result['ans'])
    print("intercept : ",result['intercept'])
    print("coefficent", result['coefficient'])