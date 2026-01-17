def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("it is odd number")

def main():
    CheckEven(21)       # positional arguement
    CheckEven(No = 22)  # keyword arguement


if(__name__ == "__main__"):
    main()