def main():

    try:
        fobj = open("Hello.txt","w")        # File handle stored in fobj(fd) and create new file
        print("File Gets successfully opened")

        fobj.write("Jay Ganesh Marvellous...")       # gave file handle to write

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    
    finally:
        print("End of application")

if __name__ == "__main__":  
    main()