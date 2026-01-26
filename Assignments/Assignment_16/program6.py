def Check(no):

    if(no > 0):
        print("It is Positive Number")
    elif(no < 0):
        print("It is negative number")
    else:
        print("It is zero number")


def main():

    Check(10)
    Check(-10)
    Check(0)


if __name__ == "__main__":
    main()