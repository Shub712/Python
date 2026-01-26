def Length(Data):

    Ans = 0
    Ans = len(Data)
    
    return Ans
def main():
    
    Value = input("Enter The String: ")
    Ret = Length(Value)
    print(Ret)

if __name__ == "__main__":
    main()