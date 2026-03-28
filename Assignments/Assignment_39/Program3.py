import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    
    df = pd.read_csv("student_performance.csv")
    
    print(df.shape)
    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']
    
    print(X.shape)
    print(Y.shape)
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2)
    
    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)
    
    model = DecisionTreeClassifier(max_depth=3)
    model.fit(X_train,Y_train)
    
    Y_pred = model.predict(X_test)
    
    print("Actual value : ")
    print(Y_test)
    
    print("Predicted Values : ")
    print(Y_pred)
    
    acc = accuracy_score(Y_test,Y_pred)
    
    print("Accuracy of the model is : ", acc*100)
            
if __name__ == "__main__":
    main()