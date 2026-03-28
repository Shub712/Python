import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    df = pd.read_csv("student_performance.csv") 

    plt.scatter(df["AssignmentsCompleted"],df["FinalResult"])
    plt.xlabel("AssignmentsCompleted")
    plt.ylabel("FinalResult")
    
    plt.show()    
    
    # Observation : Those who have completed 5 or less than 5 assignments are failed
    # and Those who have completed 5 or more assignments are passing 
    
if __name__ == "__main__":
    main()