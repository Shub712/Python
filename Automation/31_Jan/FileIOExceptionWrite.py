def main():
    try:
        open("Hello.txt","w") # create new file 
        print("File Gets successfully opened")

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    
    finally:
        print("End of application")

if __name__ == "__main__":
    main()