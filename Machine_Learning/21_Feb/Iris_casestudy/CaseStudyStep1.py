import pandas as pd         # For data Manipulation

import matplotlib.pyplot as plt     # For visualization

import seaborn as sns               # For visualization

from sklearn.model_selection import train_test_split    

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,     # To calculate mmodels accuracy
    confusion_matrix,   # Confusion Matrix
    classification_report,  # For report generation
    ConfusionMatrixDisplay  # for showing confusion matrix
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
#  STEP 2 : LOAD THE DATASET
##########################################################################

print(Border)
print("Step 1 : Load The Dataset")
print(Border)
