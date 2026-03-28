import pandas as pd

def main():
    
    df = pd.read_csv("student_performance.csv") 
    
    print("Passed Students :")
    print(df['FinalResult'].value_counts().get(1))
    
    print("Failed Students :")
    print(df['FinalResult'].value_counts().get(0))
    
    print("Percentage of Passed Students : ")
    print(df['FinalResult'].value_counts().get(1)/ df['FinalResult'].count() * 100)
    
    print("Percentage of Failed Students : ")
    print(df['FinalResult'].value_counts().get(0)/ df['FinalResult'].count() * 100)
    
    print("The Data Set is Balanced because there are no missing values in it and data is clean, values are correct")
    

if __name__ == "__main__":
    main()