import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousClassifier(Datapath):
    Border = "-"*40
    
    # Step 1 :  Load The Dataset From CSV File
    
    print(Border)
    print("Step 1 :  Load The Dataset From CSV File")
    print(Border)
    
    df = pd.read_csv(Datapath)
    
    print(Border)
    print("Some Entries from dataset")
    print(df.head())
    print(Border)
    
    # Step 2 :  Clean The Dataset by Removing empty cell
    
    print(Border)
    print("Step 2 :  Clean The Dataset by Removing empty cell")
    print(Border)
    
    df.dropna(inplace = True)
    
    print("Total Records : ", df.shape[0])
    print("Total Columns : ", df.shape[1])
    print(Border)
    
    
def main():
    Border = "-"*40
    
    print(Border)
    print("Wine Classifirs Using KNN")
    print(Border)
    
    MarvellousClassifier("WinePredictor.csv")
    
if __name__ == "__main__":
    main()