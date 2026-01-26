def CheckPrime(No):

    if No < 2:
        return False
    
    for i in range(2,int(No/2)+1):
        if No % i == 0:
            return False

    return True

def main():
    pass

if __name__ == "__main__":
    main()