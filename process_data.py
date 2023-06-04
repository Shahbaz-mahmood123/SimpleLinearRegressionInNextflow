# process_data.py
import sys
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def importData(input_data):
    dataset = pd.read_csv(input_data)
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values  
    return x, y

if __name__ == "__main__":
    input_data = sys.argv[1]
    #get the data from the CSV and get the feature and dependent variable
    x, y = importData(input_data)
    #Seperate and create the test training set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2 , random_state= 0)

    #train the linear regression model
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    # predicted_result = regressor.predict(x_test)
    

    #plot using the training data
    plt.scatter(x_train, y_train, color ='red')
    plt.plot(x_train, regressor.predict(x_train), color ='blue')
    plt.title('salary vs experience (Training set)')
    plt.xlabel('years of experience')
    plt.ylabel('Salary')
    plt.savefig('Training_plot.png')
    plt.show()
    
    #Plot test data
    plt.scatter(x_test, y_test, color ='red')
    plt.plot(x_train, regressor.predict(x_train), color ='blue')
    plt.title('salary vs experience (Test set)')
    plt.xlabel('years of experience')
    plt.ylabel('Salary')
    plt.savefig('Test_plot.png')
    plt.show()
 
    

