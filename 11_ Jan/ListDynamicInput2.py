def main():
    Size = 0

    print("Enter The Number of Elements :")
    Size = int(input())

    Data = list()
    Value = 0

    print("Enter The Elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Sum = 0

    for i in range(Size):
        Sum = Sum + Data[i]

    print("Summation is : ", Sum)

if __name__ == "__main__":
    main()