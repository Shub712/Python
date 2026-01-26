def ChkNum(No):
    
    if(No %2 == 0):
        return True
    
    else :
        return False

def main():
    bRet = ChkNum(3)

    if(bRet == True):
        print("Number is Even")
    else:
        print("Number is odd")


if __name__ == "__main__":
    main()