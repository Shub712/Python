import pandas as pd

def main():
    df = pd.read_csv("student_performance.csv") 
    
    print("Total Number of students : ")
    print(df['FinalResult'].count())
    
    print("Number of Students Passed : ")
    print(df['FinalResult'].value_counts().get(1))
    
    print("Number Of Students Failed : ")
    print(df['FinalResult'].value_counts().get(0))
if __name__ == "__main__":
    main()