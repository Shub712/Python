
def main():
    Ans  = 0
    try:
        print("inside try block")

        print("Enter First number :")
        No1 = int(input())

        print("Enter Second number :")
        No2 = int(input())

        Ans = No1 / No2

    except:
        print("inside Except")
        
    finally:
        print("Inside Finally")

    print("Divsion is : ", Ans) 

if __name__ == "__main__":
    main()