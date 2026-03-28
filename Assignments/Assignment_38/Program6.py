import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    
    df = pd.read_csv("student_performance.csv") 
    
    sns.histplot(df['StudyHours'])
    
    plt.show()

    # Histogram tells you the distribution of the data,
    # The given input of "StudyHours" which is describing 
    # the range of the study hours and how many students appears in
    # that range on the X axis are the Study hours and on the Y axis are the
    # count of students who falls in that range
    
if __name__ == "__main__":
    main()