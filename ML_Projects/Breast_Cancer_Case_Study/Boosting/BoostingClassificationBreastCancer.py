import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
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
# Step 4 : Create Boosting Model Adaboost
#---------------------------------------------------------

boost_model = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=1.0,
    random_state=42)


#---------------------------------------------------------
# Step 5 : Train boosting Model
#---------------------------------------------------------

boost_model.fit(X_train,Y_train)

#---------------------------------------------------------
# Step 6 : Test boosting model
#---------------------------------------------------------

y_pred = boost_model.predict(X_test)

#---------------------------------------------------------
# Step 7 : Evaluate  boosting model
#---------------------------------------------------------

accr = accuracy_score(y_pred,Y_test)

print("Boosting Accuracy : ",accr*100)

print("Confusion Matrix : ")
print(confusion_matrix(Y_test,y_pred))