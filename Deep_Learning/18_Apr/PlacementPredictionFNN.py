#-----------------------------------
# Import Required Libraries
#-----------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

#------------------------------------------------------------
# Step 1 : Load Dataset From csv
#------------------------------------------------------------

print("Step 1 : Loading Dataset....\n")

data = pd.read_csv("placement_data.csv")

print("Complete Dataset")
print(data)

#------------------------------------------------------------
# Step 2 : Understand The Dataset
#------------------------------------------------------------

print("\nStep 2 : Basic Information")
print("\nFirst 5 Records")
print(data.head())

print("\nDataset Shape :")
print(data.shape)

print("\nColumn Names :")
print(data.columns)

print("\nStatistical Summary :")
print(data.describe())

print("\nChecking Missing Values :")
print(data.isnull().sum())


#------------------------------------------------------------
# Step 3 : Seperate Input Feature and Target output
#------------------------------------------------------------

print("\nStep 3 : Splitting input and output")

# X = Input Features
X = data[["Aptitude","Coding","Communication","Academics","Internship"]]

# y = Target Output
y =data["Placed"]

print("\nInput Features (X):")
print(X.head())

print("\nTarget Output (y) :")
print(y.head())

#------------------------------------------------------------
# Step 4 : Train-Test Split
#------------------------------------------------------------
print("\nStep 4: Splitting into training and testing data")

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print("\nTraining input shape : ",X_train.shape)
print("Testing Input Shape :",X_test.shape)
print("Training Output Shape : ",y_train.shape)
print("Testing Ouput Shape : ",y_test.shape)

#------------------------------------------------------------
# Step 5 : Feature Scalling
# Neural Networks usually perform better when inputs are scaled
#------------------------------------------------------------

print("\nStep 5 : Scaling the input features")
scaler = StandardScaler()

X_train_Scaled = scaler.fit_transform(X_train)
X_test_Scaled = scaler.fit_transform(X_test)

print("\nScaled Training Data Sample:")
print(X_train_Scaled[:5])

#------------------------------------------------------------
# Step 6 : Create Feed Forward Neural Network Model
# hiddwn_layer_size = (8,4)
# means:
#   first hidden layer -> 8 neurons(perceptrons)
#   second hidden layer -> 4 neurons(perceptrons)
# activation = 'relu' means ReLU will be used
# max_iter = 1000 means model can train upto 1000 iterations
#------------------------------------------------------------

print("\nCreating FNN Model...")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)    

print(model)

#------------------------------------------------------------
# Step 7 : Train The Model
#------------------------------------------------------------

print("\nStep 7 : Training The Model...")
model.fit(X_train_Scaled,y_train)

print("\nModel Training Completed")

#------------------------------------------------------------
# Step 8 : Make Prediction on testing data
#------------------------------------------------------------

y_pred = model.predict(X_test_Scaled)

print("\nActual Output :")
print(y_test.values)

print("\nPredicted Output:")
print(y_pred)

#------------------------------------------------------------
# Step 9 : Evaluate Model Performance
#------------------------------------------------------------

print("\nStep 9 : Model Evaluation")

accuracy= accuracy_score(y_test,y_pred)
print("\nAccuracy  is : ",accuracy*100,"%")

cm = confusion_matrix(y_test,y_pred)
print("\nConfusion Matrix :")
print(cm)

print("\nClassification Report:")
print(classification_report(y_test,y_pred))

#------------------------------------------------------------
# Step 10 : Predict Probablity
# predict_proba gives confidence scores
#------------------------------------------------------------

print("\nStep 10: Prediction Probablities:")
y_prob = model.predict_proba(X_test_Scaled)

print(y_prob[:5])\

#------------------------------------------------------------
# Step 11 : Save Model and Scaler
# This is called model preservation
#------------------------------------------------------------

print("\nStep 11 : Saving Model and scaler")

joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scaler,"placement_scaler.pkl")

print("\nModel Saved as : placement_fnn_model.pkl")
print("\nScaler saved as : placement_scaler.pkl")

#------------------------------------------------------------
# Step 12 : Load Model and Scaler Again
#------------------------------------------------------------

print("\nStep 12 : Loading Saved Model and Scaler")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scaler = joblib.load("placement_scaler.pkl")

print("\nSaved model and scaler loaded successfully")

#------------------------------------------------------------
# Step 13 : Predict For New Student
# Example:
# Aptitude : 70
# Coding : 72
# Communication : 75
# Academics : 74
# Internship : 1
#------------------------------------------------------------

print("\nStep 13 : Prediction New Student")

new_student = pd.DataFrame([[70,72,75,74,1]],columns=["Aptitude","Coding","Communication","Academics","Internship"])
new_student_scaled = loaded_scaler.transform(new_student)

new_prediction=loaded_model.predict(new_student_scaled)
new_probablity = loaded_model.predict_proba(new_student_scaled)

print("\nNew Student Data:")
print(new_student)

if new_prediction[0] == 1:
    print("\nPrediction : PLACED")
else:
    print("\nPrediction : NOT PLACED")

print("Prediction Probablity :",new_probablity)

#------------------------------------------------------------
# Step 1 : Load Dataset From csv
#------------------------------------------------------------
