import pandas as pd

def main():
    df = pd.read_csv("student_performance.csv") 
    
    print("Average Study Hours : ")
    print(df['StudyHours'].mean())
    
    print("Average Attendance : ")
    print(df['Attendance'].mean())
    
    print("Maximum Previous Score : ")
    print(df['PreviousScore'].max())
    
    print("Minimum Sleep Hours : ")
    print(df['SleepHours'].min())

if __name__ == "__main__":
    main()