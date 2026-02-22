from sklearn.datasets import load_iris

def main():
    
    Border = "-"*40
    
    print("Iris Classification case study")
    
    # Metadata of dataset
    DataSet = load_iris()
    
    print(Border)

    for i in range(len(DataSet.target)):
        print("ID %d , Features %s , label %s" %(i,DataSet.data[i],DataSet.target[i]))
        
    print(Border)

if __name__ == "__main__":
    main()