import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    df = pd.read_csv("student_performance.csv") 

    plt.scatter(df["SleepHours"],df["FinalResult"])
    plt.xlabel("SleepHours")
    plt.ylabel("FinalResult")
    
    plt.show()    
    
    # Observation : The Sleeping Hours is not affecting the final result 
    
if __name__ == "__main__":
    main()