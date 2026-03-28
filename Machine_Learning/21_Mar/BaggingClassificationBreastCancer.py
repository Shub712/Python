import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#---------------------------------------------------------
# Step 1 : Load The Dataset
#---------------------------------------------------------

df = pd.read_csv("Breast_cancer.csv")

print("Shape of dataset : ",df.shape)
print("First 5 records : ",df.head())

#---------------------------------------------------------
# Step 2 : Seperate features and labels
#---------------------------------------------------------

X = df.drop("target",axis=1)  # feature
Y =df["target"] # label

#---------------------------------------------------------
# Step 3 : Split dataset for training and testing
#---------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#---------------------------------------------------------
# Step 4 : Create Base Model
#---------------------------------------------------------

base_model = DecisionTreeClassifier(random_state=42)

#---------------------------------------------------------
# Step 5 : Create Bagging Model
#---------------------------------------------------------

bagging_model = BaggingClassifier(
    estimator=base_model,
    n_estimators=10,
    random_state=42
)

#---------------------------------------------------------
# Step 6 : Train Bagging Model
#---------------------------------------------------------

bagging_model.fit(X_train,Y_train)

#---------------------------------------------------------
# Step 7 : Test bagging model
#---------------------------------------------------------

y_pred = bagging_model.predict(X_test)

#---------------------------------------------------------
# Step 8 : Evaluate the model
#---------------------------------------------------------

accr = accuracy_score(y_pred,Y_test)

print("Accuracy : ",accr*100)

print("Confusion Matrix : ")
print(confusion_matrix(Y_test,y_pred))