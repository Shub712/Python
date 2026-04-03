import os

KEY = 0x11
HEADER_SIZE = 100

def Decrypt_data(data):
    
    result = bytearray()
    
    for b in data:
        result.append(b ^ KEY)
    
    return result

def Unpack_file(packed_file):
    
    if not os.path.exists(packed_file):
        print("There is no such pack file")
        return
    
    with open(packed_file,"rb") as f :
        
        while True:
            
            # Read the header            
            header_bytes = f.read(HEADER_SIZE)
            
            if not header_bytes:
                break # end of file
            
            # Converts bytes -> string
            header = header_bytes.decode().strip()   # strip() removes the extra space from the both ends of the string

            #  Split Filename and size 
            tokens = header.split(" ")
            
            filename = tokens[0]
            filesize = int(tokens[1])
            
            print(f"File Name : {filename}")
            print(f"File Size : {filesize}")
            
            #read Encrypted data header = header_bytes.decode().strip()
            data = f.read(filesize)
            
            # decrypt data
            
            decrypted = Decrypt_data(data)
            
            # Write Original File
            output_dir = os.path.dirname(packed_file)
            output_path = os.path.join(output_dir,filename)
            
            with open(filename,"wb") as out_file :
                
                out_file.write(decrypted)
    
    print("Unpacking Completed!!")
    
def main():
  packed = input("Enter packed file name : ")
  Unpack_file(packed)
  
if __name__ == "__main__":
    main()