def main():

    try:
        fobj = open("Hello.txt","r")        # File handle stored in fobj(fd) and create new file
        print("File Gets successfully opened")

        Data = fobj.read()      # to read

        print("Data from file is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    
    finally:
        print("End of application")

if __name__ == "__main__":  
    main()