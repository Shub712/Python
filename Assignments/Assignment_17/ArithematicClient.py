from ArithematicModule import *

def main():

    Value1 = int(input("Enter The first Number : "))
    Value2 = int(input("Enter The second number : "))

    Ret = Add(Value1,Value2)
    print("Addition is : ", Ret)

    Ret = Sub(Value1,Value2)
    print("Substraction is : ", Ret)

    Ret = Mult(Value1,Value2)
    print("Multiplication is : ", Ret)

    Ret = Div(Value1,Value2)
    print("Division is : ", Ret)

if __name__ == "__main__":
    main()