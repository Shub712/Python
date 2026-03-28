import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error,r2_score

#---------------------------------------------------------
# Step 1 : Load The Dataset
#---------------------------------------------------------

df = pd.read_csv("California_housing.csv")

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
# Step 4 : Create gradient boosting Model
#---------------------------------------------------------

boost_model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42)


#---------------------------------------------------------
# Step 5 : Train Boosting Model
#---------------------------------------------------------

boost_model.fit(X_train,Y_train)

#---------------------------------------------------------
# Step 6 : Test Boosting model
#---------------------------------------------------------

y_pred = boost_model.predict(X_test)

#---------------------------------------------------------
# Step 7 : Evaluate Boosting model
#---------------------------------------------------------

print("Mean Sqaured Error : ",mean_squared_error(Y_test,y_pred))
print("R sqaure : ",r2_score(Y_test,y_pred))    