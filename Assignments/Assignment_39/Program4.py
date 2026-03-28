import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay

def main():
    
    # Load The CSV
    
    df = pd.read_csv("student_performance.csv")
    
    # Split in into 2 parts independant variable and dependant variable
    
    print(df.shape)
    X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
    Y = df['FinalResult']
    
    print(X.shape)
    print(Y.shape)
    
    # Split it into 4 parts for training and testing
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5)
    
    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)
    
    model = DecisionTreeClassifier()
    model.fit(X_train,Y_train)
    
    # Train The Model
    
    Y_pred = model.predict(X_test)
    
    # Comparing the predicted and actual values 
    
    print("Actual value : ")
    print(Y_test)
    
    print("Predicted Values : ")
    print(Y_pred)
    
    # Calculate the accuracy of the model
    
    acc = accuracy_score(Y_test,Y_pred)
    
    print("Accuracy of the model is : ", acc*100)
    
    # Ploting The Confusion Matrix
    
    cm = confusion_matrix(Y_pred,Y_test)
    print("Confusion Matrix")
    print(cm)
    
    data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
    
    data.plot()
    plt.title("Confusion Matrix of Student Performance Dataset")
    plt.show()
    
if __name__ == "__main__":
    main()