def main():

    try:
        fobj = open("Hello.txt","a")        # File handle stored in fobj(fd) and create new file with append
        print("File Gets successfully opened")

        fobj.write("Python Automation")       # gave file handle to write

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    
    finally:
        print("End of application")

if __name__ == "__main__":  
    main()