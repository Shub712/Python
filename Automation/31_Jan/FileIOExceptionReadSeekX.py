#seek(kuthe,kuthun)
# Kuthun : 0/1 / 2
# 0 : Starting
# 1 : Current
# 2 : End


def main():

    try:
        fobj = open("Hello.txt","r")        # File handle stored in fobj(fd) and create new file
        print("File Gets successfully opened")

        print("Cuurent Offset : ",fobj.tell())  # 0

        fobj.seek(7,0)

        print("Cuurent Offset : ",fobj.tell())  # 7

        Data = fobj.read(10)                # to read

        print("Cuurent Offset : ",fobj.tell())  # 17

        print("Data from file is : ",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    
    finally:
        print("End of application")

if __name__ == "__main__":  
    main()