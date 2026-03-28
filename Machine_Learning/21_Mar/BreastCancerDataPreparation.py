import pandas as pd
from sklearn.datasets import load_breast_cancer


def main():
    Data = load_breast_cancer()
    
    df = pd.DataFrame(Data.data,columns=Data.feature_names)
    df["target"] = Data.target
    
    df.to_csv("Breast_cancer.csv",index=False)
    
    print("Breast_cancer.csv file gets created successfully")
if __name__ == "__main__":
    main()