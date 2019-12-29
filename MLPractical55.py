import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import warnings
warnings.filterwarnings(action="ignore")

# Function to get data
def get_data(file_name):
    dataframe = pd.read_csv(file_name)
    print(dataframe)
    x_parameters = []
    y_parameters = []
    for single_square_feet,single_price_value in zip(
        dataframe['square_feet'],dataframe['price'] ):
        x_parameters.append( [ float(single_square_feet) ] )   # [] is for multivariate input, here is univariate input
        y_parameters.append(  float(single_price_value)  )

    return x_parameters,y_parameters

# Function for fitting data to Linear model
def linear_model_main(X_parameters,Y_parameters,quest_value):
    # Create linear regression object
    regr = LinearRegression()
    print( "AREA : ", X_parameters)
    print( "PRICE : ",Y_parameters)
    regr.fit(X_parameters,Y_parameters)  # model formed by training data
    # Hypothesis parameter(m,c) are stored in hidden(internal variable) variable of object
    predicted_ans = regr.predict( [ [quest_value] ] )
    predictions = {}
    predictions['coefficient'] = regr.coef_      # this is the hidden variable of m
    predictions['intercept'] = regr.intercept_   # this is the hidden variable of c
    predictions['predicted_ans']=predicted_ans

    print("Output from Machine = ",predicted_ans)
    plt.scatter(X_parameters,Y_parameters,color = "m",marker = "o", s=30)
    all_predicted_Y = regr.predict(X_parameters)
    plt.scatter(X_parameters,all_predicted_Y,color="b")
    plt.plot(X_parameters,all_predicted_Y,color="r")
    plt.scatter(quest_value,predicted_ans,color = "g")
    plt.show()
    return predictions

# predicting house price for house of 700 square feet area
if __name__ == "__main__":
    x,y = get_data('LR_House_price.csv')
    print(type(x))
    question_value = 700 # This is the question
    result= linear_model_main(x,y,question_value)
    print( "Intercept value ",result['intercept'] )
    print( "coefficient", result['coefficient'] )
    print( "Predicted House Price value: ",result['predicted_ans'] )
