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
    
    
def main():
    MarvellousAdvertise("Advertising.csv")

if __name__  == "__main__":
    main()
    