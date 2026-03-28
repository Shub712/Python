import pandas as pd
from sklearn.datasets import fetch_california_housing


def main():
    Data = fetch_california_housing()
    
    df = pd.DataFrame(Data.data,columns=Data.feature_names)
    df["target"] = Data.target
    
    df.to_csv("California_housing.csv",index=False)
    
    print("California_housing.csv file gets created successfully")
if __name__ == "__main__":
    main()