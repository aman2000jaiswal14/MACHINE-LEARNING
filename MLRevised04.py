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



def get_data(filename):
    x_parameters=[]
    y_parameters=[]
    dataframe = pd.read_csv(filename)
    for single_square_feet, single_price_value in zip(
            dataframe['x'], dataframe['y']):
        x_parameters.append([float(single_square_feet)])  # [] is for multivariate input, here is univariate input
        y_parameters.append(float(single_price_value))

    return x_parameters, y_parameters
if __name__ == '__main__':
    x,y = get_data('mydata5.csv')
    quest = [4]
    result = linear_model_main(x,y,quest)
    print("result[coefficient]  :  ",result['coefficient'])
    print("result[intercept]   :  ",result['intercept'])
    print("result[ans]   :   ",result['ans'])




