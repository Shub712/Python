import os

KEY = 0x11
HEADER_SIZE = 100
BUFFER_SIZE = 1024

def Create_header(file_name,file_size):
    
    header = f"{file_name} {file_size}"
    header = header.ljust(HEADER_SIZE) # Padding with spaces
    
    return header.encode()   # Converts String into Byte 

def Encrypt_data(data):
    
    result = bytearray()
    
    for b in data:
        result.append(b ^ KEY)

    return result
    #return bytearray([b ^ KEY for b in data])


def pack_folder(folder_name,pack_name):
    
    if not os.path.exists(folder_name) or not os.path.isdir(folder_name): # Checked if folder exists or not
        print("THERE IS NO SUCH FOLDER!!!")
        return
    
    
    files = os.listdir(folder_name)   # stored list of files from the folder
    
    print(f"Number of files : {len(files)}")
    
    with open(pack_name,"wb") as pack_file:
        
        for file in files:
            
            print("Checking : ",file)
            
            if(file.endswith(".txt")):
                print("packing File : ", file)
                
                file_path = os.path.join(folder_name,file)
                file_size = os.path.getsize(file_path)
                
                # Create Header
                header = Create_header(file,file_size)
                pack_file.write(header)
                
                # read and encrypt the file data
                
                with open(file_path,"rb") as f :
                    while True:
                        buffer = f.read(BUFFER_SIZE)
                        
                        if not buffer:
                            break
                        
                        encrypted = Encrypt_data(buffer)
                        
                        pack_file.write(encrypted)
    
    print("Packing Completed Successfully!")
    
def main():
    
    folder = input("Enter Folder Name : ")
    pack = input("Enter Name For PackFile : ")
    
    pack = pack + ".pak"
    pack_folder(folder,pack)

if __name__ == "__main__":
    main()