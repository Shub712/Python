import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler 

def MarvellousClassifier(Datapath):
    Border = "-"*40
    
    # Step 1 :  Load The Dataset From CSV File
    
    print(Border)
    print("Step 1 :  Load The Dataset From CSV File")
    print(Border)
    
    df = pd.read_csv(Datapath)
    
    print(Border)
    print("Some Entries from dataset")
    print(df.head())
    print(Border)
    
    # Step 2 :  Clean The Dataset by Removing empty cell
    
    print(Border)
    print("Step 2 :Clean The Dataset by Removing empty cell")
    print(Border)   
    
    df.dropna(inplace = True)
    
    print("Total Records : ", df.shape[0])
    print("Total Columns : ", df.shape[1])
    print(Border)
    
    # Step 3 :  Seperate Independant & Dependant variables
    
    print(Border)
    print("Step 3 : Seperate Independant & Dependant variables")
    print(Border)
    
    X = df.drop(columns=['Class'])
    Y = df['Class']
    
    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)
    
    print(Border)
    print("Input Columns : ", X.columns.to_list())
    print("Output Column : Class")
    
    # Step 4 :  Split The dataset for trainng and testing
    
    print(Border)
    print("Step 4 : Split The dataset for trainng and testing")
    print(Border)
    
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)
    
    print(Border)
    print("INformation of Training and testing data")
    print("X_train Shape : ", X_train.shape)
    print("X_test Shape : ", X_test.shape)
    print("Y_train Shape : ", Y_train.shape)
    print("Y_test Shape : ", Y_test.shape)
        
    # Step 5 : Feature Scaling
    
    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)
    
    Scaler = StandardScaler()
    
    # Independant Variable scaling
    X_train_scaled = Scaler.fit_transform(X_train)
    X_test_scaled = Scaler.fit_transform(X_test)
    
    print("Feature Scaling is done")
    
    # Step 6 : Explore the multiple values of k
    # Hyperparameter tuning (K)
    
    accuracy_scores = []
    K_values = range(1,21)
    
    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)
    
    print(Border)
    print("Accuracy Report value from 1 to 20 : ")
    
    for value in accuracy_scores:
        print(value)
        
    print(Border)
    
    # step 7 : Plot graph of k vs accuracy
    
    print(Border)
    print("Step 7 : Plot graph of K vs Accuracy")
    print(Border)
    
    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.title("K Values vs Accuracy")
    plt.xlabel("Value Of K")
    plt.ylabel("Accuracy")
    
    plt.grid(True)
    plt.xticks(list(K_values))
    plt.show()
    
    # Step 8 : Find Best Value Of K 
    print(Border)
    print("Step 8 : Find Best Valur of K")
    print(Border)
    
    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]
    
    print("Best Value of K is : ",best_k)
    
    # Setp 9 : Build Final Model using best value of k
    
    print(Border)
    print("Step 9 : Build Final Model using best value of k")
    print(Border)
    
    final_model  = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled,Y_train)
    Y_pred = final_model.predict(X_test_scaled)
    
    # step 10 : Calculate Final accuracy
    print(Border)
    print("Step 10 : Calculate Final accuracy")
    print(Border)
    
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of the model is : ", accuracy*100 )
    
    # Step 11 : Display Confusion matrix
    print(Border)
    print("Step 11 : Dsiplay Confusion matrix")
    print(Border)
    
    cm = confusion_matrix(Y_test,Y_pred)
    
    print(cm)
    
    # Step 12 : Display classification report
    print(Border)
    print("Step 12 : Display Classification report")
    print(Border)
    
    print(classification_report(Y_test,Y_pred))
    
def main():
    
    Border = "-"*40
    
    print(Border)
    print("Wine Classifirs Using KNN")
    print(Border)
    
    MarvellousClassifier("WinePredictor.csv")
    
if __name__ == "__main__":
    main()