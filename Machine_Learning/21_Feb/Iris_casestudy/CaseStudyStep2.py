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
print(df.head())

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



