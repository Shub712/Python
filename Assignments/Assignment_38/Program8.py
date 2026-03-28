import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    df = pd.read_csv("student_performance.csv") 

    plt.boxplot(df["Attendance"])
    plt.show()
    
if __name__ == "__main__":
    main()