import pandas as pd

def main():
    df = pd.read_csv("student_performance.csv") 
    
    print("First 5 Records are : ")
    print(df.head())
    print("Last 5 records are : ")
    print(df.tail())
    
    print("Total Number of rows and columns :")
    print(df.shape)

    print("Column Names : ")
    print(df.columns)
    
    print(df.dtypes)
    
       
if __name__ == "__main__":
    main()