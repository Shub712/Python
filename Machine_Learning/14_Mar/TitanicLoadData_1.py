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