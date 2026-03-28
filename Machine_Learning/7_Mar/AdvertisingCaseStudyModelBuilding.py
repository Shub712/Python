import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdvertise(datapath):
    border = "-"*40
    #----------------------------------------------------------
    # Step 1 : Load The Dataset
    #----------------------------------------------------------
    
    print(border)
    print("Step 1 : Load Dataset")
    print(border)
    
    df = pd.read_csv(datapath)
    
    print("Few Records From the dataset :")
    print(df.head())
    
    #----------------------------------------------------------
    # Step 2 : Remove Unwanted Columns
    #----------------------------------------------------------
    
    print(border)
    print("Step 1 : Load Dataset")
    print(border)
    
    print("Shape of dataset before removal : ",df.shape)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
    
    print("Shape of dataset after removal : ", df.shape)
    
    print(border)
    print("Clean dataset is :")
    print(border)
    
    print(df.head())
    
    #----------------------------------------------------------
    # Step 3 : Check missing values
    #----------------------------------------------------------
    
    print(border)
    print("Step 3 : Check Missing Values")
    print(border)
    
    print("Missing values count : \n",df.isnull().sum())
    
    #----------------------------------------------------------
    # Step 4 : Display Statiscal Summary
    #----------------------------------------------------------
    
    print(border)
    print("Step 4 : Display Statistical Summary")
    print(border)
    
    print(df.describe)
        
    #----------------------------------------------------------
    # Step 5 : Correlation between columns
    #----------------------------------------------------------
    
    print(border)
    print("Step 5 : Corelation between column")
    print(border)
    
    print("Correlation Matrix")
    print(df.corr())
    
    #----------------------------------------------------------
    # Step 6 : Split Dataset Into Independant & Dependant variable
    #----------------------------------------------------------
    
    print(border)
    print("Step 6 : Split Dataset Into Independant & Dependant variable")
    print(border)
    
    X = df[['TV','radio','newspaper']] 
    Y = df['sales']
    
    print("Shape of Independant Variables : ", X.shape)
    print("Shape of Dependant Variables : ", Y.shape)
    
    #----------------------------------------------------------
    # Step 7 : Split Dataset For Training & Testing
    #----------------------------------------------------------
    
    print(border)
    print("Step 7 : Split Dataset For Training & Testing")
    print(border)
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size= 0.2,random_state=42)
    
    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)
    print("Y_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)

    #----------------------------------------------------------
    # Step 8 : Create & train The Model
    #----------------------------------------------------------
    
    print(border)
    print("Step 8 : Create & train the  model")
    print(border)
    
    model = LinearRegression()
    model.fit(X_train,Y_train)
    
    #----------------------------------------------------------
    # Step 9 : Test the model
    #----------------------------------------------------------
    
    print(border)
    print("Step 9 : Test The Model")
    print(border)
    
    Y_pred = model.predict(X_test)
    
    #----------------------------------------------------------
    # Step 10 : Evaluate The Model
    #----------------------------------------------------------
    
    print(border)
    print("Step 20 : Evaluate The Model")
    print(border)
    
    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE) 
    R2 = r2_score(Y_test,Y_pred)
    
    print("Mean Squared Error :", MSE)
    print("Root Mean Squared Error : ", RMSE)
    print("R square value : ",R2)
    
    #----------------------------------------------------------
    # Step 11 : Calculate Model Coefficient
    #----------------------------------------------------------
    
    print(border)
    print("Step 11 : Calculate model coefficient")
    print(border)
    
    for column , value  in zip(X.columns,model.coef_):
        print(f"{column} : {value}")
        
    print("Intercept : ",model.intercept_)
    
    #----------------------------------------------------------
    # Step 12 : Compare the actual and predicted values
    #----------------------------------------------------------
    
    print(border)
    print("Step 12 : Compare the actual and predicted values")
    print(border)
    
    Result = pd.DataFrame({'Actual sale' : Y_test.values,
                           'Predicted Sale' : Y_pred
                           })
    print(Result.head())
    
def main():
    MarvellousAdvertise("Advertising.csv")

if __name__  == "__main__":
    main()
    