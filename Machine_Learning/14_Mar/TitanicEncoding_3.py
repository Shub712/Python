import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
#-------------------------------------------------------------------------
#  Function Name : DisplayInfo
#  Description :   It displays the formated title
#  Parameters :    title(str)
#  Return :        None
#  Date :          14/03/2026
#  Author :        Shubham Kiran Pawar
#-------------------------------------------------------------------------

def DisplayInfo(title):
    
    print("\n"+"="*70)
    print(title)
    print("="*70)
    
#-------------------------------------------------------------------------
#  Function Name :  CleanTitanicData
#  Description :    it does preprocessing 
#                   it removes unnecessary columns
#                   it handles missing values
#                   it converts text data to numeric format
#                   it does encoding to categorical columns
#  Parameters :     df -> pandas dataframe     
#  Return :         df -> clened pandas dataframe
#  Date :           14/03/2026
#  Author :         Shubham Kiran Pawar
#-------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Oroginal Data")
    print(df.head())
    
    # Remove unnecessary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]
    print("\n Columns to be dropped : ")
    print(existing_columns)
    
    # Drop the unwanted columns
    df = df.drop(columns = existing_columns)
    DisplayInfo("Step 2 : Data After column removal")
    print(df.head())
    
    # Handle Age Column
    if "Age" in df.columns:
        print("Age Column before filling missing values")  
        print(df["Age"].head(10))  
        
        # coerce = Invalid values gets converted as NaN
        df["Age"]=pd.to_numeric(df["Age"],errors = "coerce") 
        
        age_median = df["Age"].median()
        
        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)
        
        print("\nAge COlumn after preprocessing :")
        print(df["Age"].head(10))
    
    # Handle Fare Column
    
    if "Fare" in df.columns:
        print("\n Fare Column Before pre processing" )
        print(df["Fare"].head(10))
        df["Fare"]=pd.to_numeric(df["Fare"],errors = "coerce") 
        
        fare_median = df["Fare"].median()
        print("\n Median fo fare column ; ",fare_median)
        
        # Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)
        
        print("\n Fare Column after preprocessing ")
        print(df["Fare"].head(10))
        
    # Handle Embarked column
    
    if "Embarked" in df.columns:
        print("\n Embarked Column before preprocessing :")
        print(df["Embarked"].head(10))
        
        # Convert The data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()
        
        # Remove missing values 
        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)
        
        # Get Most Frequent value
        embarked_mode = df["Embarked"].mode()[0]
        
        print("Mode of Embarked column : ",embarked_mode)
        df["Embarked"] = df["Embarked"].fillna(embarked_mode)
        
        print("\n Embarked Column after preprocessing :")
        print(df["Embarked"].head(10))
    
    # Handle sex column
    
    if "Sex" in df.columns:
        print("\n Sex Column Before pre processing" )
        print(df["Sex"].head(10))
        
        df["Sex"]=pd.to_numeric(df["Sex"],errors = "coerce") 
        
        print("\n Sex Column after preprocessing :")
        print(df["Sex"].head(10))
    
    DisplayInfo("Data After Preprocessing")
    print(df.head())
    
    print("\n Missing Values After Preprocessing")
    print(df.isnull().sum())   
    
    # Encode Embarked Column
    df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)
    print("\n Data After Encoding")
    
    print(df.head())
    
    print("Shape of dataset : ",df.shape)
    
    # convert boolean columns into integer
    
    for col in df.columns:
        if(df[col].dtype == bool):
            df[col] = df[col].astype(int)
    
    DisplayInfo("Data After Preprocessing")
    print(df.head())
    
    return df

#-------------------------------------------------------------------------
#  Function Name :  Showdata
#  Description :    It shows basix information about dataset
#  Parameters :     DataSet(df),
#                   df ->       Pandas Dataframe Object
#                   Message
#                   Message ->  Heading text display
#  Return :         None
#  Date :           14/03/2026
#  Author :         Shubham Kiran Pawar
#-------------------------------------------------------------------------

def Showdata(df,message):
    DisplayInfo(message)
    print("\nFirst 5 Rows of dataset : ")
    print(df.head())
    
    print("\n Shape of dataset : ")
    print(df.shape)
    
    print("\n Column Names : ")
    print(df.columns.tolist())
    print("\n Missing Values in each column : ")
    print(df.isnull().sum())

    
#-------------------------------------------------------------------------
#  Function Name : MarvellousTitanicLogistic
#  Description :   This Main pipeline controller 
#                  It loads the dataset, shows raw data,
#                  it preprocess dataset & train the model
#  Parameters :    Data path of dataset file
#  Return :        None
#  Date :          14/03/2026
#  Author :        Shubham Kiran Pawar
#-------------------------------------------------------------------------
 
def MarvellousTitanicLogistic(datapath):
    DisplayInfo("Step 1 : Loading The Dataset")
    df = pd.read_csv(datapath)
    Showdata(df,"Initial Dataset")
    
    df = CleanTitanicData(df)

#-------------------------------------------------------------------------
#  Function Name : main
#  Description :   Staring point of the application
#  Parameters :    None
#  Return :        None
#  Date :          14/03/2026
#  Author :        Shubham Kiran Pawar
#-------------------------------------------------------------------------

def main(): 
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()