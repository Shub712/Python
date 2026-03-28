import pandas as pd

def main():
    
    df = pd.read_csv("student_performance.csv") 
    
    correlation = df.corr()
    
    print(correlation["StudyHours"].sort_values(ascending=False))
    
    # 0.850569
    
    print(correlation["Attendance"].sort_values(ascending=False))
    
    # 0.856455

if __name__ == "__main__":
    main()