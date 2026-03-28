import pandas as pd
import matplotlib.pyplot as plt

def main():
    
    df = pd.read_csv("student_performance.csv") 

    # seperate the failed Student and passstudent
    PassStudents = df[df["FinalResult"] == 1]
    FailedStudents = df[df["FinalResult"] == 0]
    
    # plot the passstudents with color green and label pass
    plt.scatter(PassStudents["StudyHours"],PassStudents["PreviousScore"],
                color = "green",label = "Pass")
    
    # plot the failed students with color red and label failed
    plt.scatter(FailedStudents["StudyHours"],FailedStudents["PreviousScore"],
                color = "red",label = "Fail")
    
    # decides the label of axis
    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    
    # Decide the title
    plt.title("StudyHours vs PreviousScore")
    plt.grid(True)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()