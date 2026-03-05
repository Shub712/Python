import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40
##########################################################################
#  STEP 1 : LOAD THE DATASET
##########################################################################

print(Border)
print("Step 1 : Load The Dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Data gets loaded successfully")
print("Intial Entries From Dataset : ")
print(df.head())        # Display First Five Entries Of the data set

##########################################################################
#  STEP 2 : DATA ANALYSIS (EDA)
##########################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column Names : ", list(df.columns))

print("Missing Values (per column)")
print(df.isnull().sum())

print("Class Destribution (Species Count)")
print(df["species"].value_counts())

print("Statistical Report Of Dataset")
print(df.describe())


##########################################################################
#  STEP 3 : DECIDE IDEPENDANT & DEPENDANT VARIABLES
##########################################################################

print(Border)
print("Step 3 : Decide Independant & Dependant Variable")
print(Border)

# X : Independant Variables / Features
# Y : Dependant Variable / Labels

feature_cols = [
    
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ", Y.shape)


##########################################################################
#  STEP 4 : VISUALIASATION OF DATASET
##########################################################################

print(Border)
print("Step 4 : Visualisation of data set")
print(Border)

# Scatterplot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"],label = sp)

plt.title("Iris : Petal length vs Petal Width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show()

##########################################################################
#  STEP 5 : SPLIT THE DATASET FOR TRAINING AND TESTING
##########################################################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

# total dataset = 150,5
# X : 150,4
# Y : 150,1
# Testingsize = 20%
# TrainingSize = 80%

X_Train, X_Test, Y_Train, Y_Test = train_test_split(
    X,
    Y,
    test_size = 0.2, # testing size
    random_state = 42   # Shuffling        
)

print("Data Spliting Activity Done")

print("X - Independant : ", X.shape)    # (150,4)
print("X - Dependant : ", Y.shape)      # (150,)

print("X_Train :", X_Train.shape)       # (120,4)
print("X_Test :", X_Test.shape)         # (30,4)

print("Y_Train :", Y_Train.shape)       # (120,)
print("Y_Test :", Y_Test.shape)         # (30,)

##########################################################################
#  STEP 6 : BUILD THE MODEL
##########################################################################

print(Border)
print("Step 6 : Build The Model")
print(Border)

print("We Are Going To Use DecisionTreeeClassifier")

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 3,
    random_state = 42    
)

print("Model Successfully created : ", model)

##########################################################################
#  STEP 7 : TRAIN THE MODEL
##########################################################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_Train,Y_Train)

print("Model Training Completed...")


##########################################################################
#  STEP 8 : TEST THE MODEL (EVALUATE)
##########################################################################

print(Border)
print("Step 8 : Evaluate The Model")
print(Border)

Y_pred = model.predict(X_Test)

print("Model Evaluation (testing) Complete...")

print(Y_pred.shape)

print("Expected answers : ")
print(Y_Test)

print("Predicted Answers : ")
print(Y_pred)
