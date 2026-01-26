import sys

def main():
    Border = "-"*42
    print(Border)
    print("---------Marvellous Automation------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This Application is used to perform ______")
            print("This is a automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as:")
            print("ScriptName.py Argument1 Argument2")
            print("Arguement1 : __________")
            print("Arguement2 : __________")

        else:
            print("Use The Given flags as : ")
            print("--u : Used to display the usage")
            print("--h : Used to display the help")

    else:
        print("Invalid Number of command line arguments")
        print("Use The Given flags as : ")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)
    print("-------Thank You For Using Our Script-----")
    print("---------Marvellous Infosystems-----------")
    print(Border)

if __name__ == "__main__":
    main()