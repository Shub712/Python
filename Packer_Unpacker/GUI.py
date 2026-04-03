import tkinter as tk  # For GUI creation 
from tkinter import filedialog,messagebox,ttk # filedoalog for file / folder picker
                                                # messagebox for popup message  
                                                #ttk for progress bar
import os             # for file handling                              


from Packer import pack_folder   # custom function
from Unpacker import Unpack_file    # custom function

def Create_gui():
    
    
    def browse_folder():
        
        folder = filedialog.askdirectory() # stored folder path inside folder
        folder_entry.delete(0,tk.END)     # Removes  old text
        folder_entry.insert(0,folder)     # insert new folder path 
        
    # it lets user chose where to save the packed file
    def browse_output():
        
        file = filedialog.asksaveasfilename(defaultextension=".pak") # opens save file window
        output_entry.delete(0,tk.END) # Removes old text
        output_entry.insert(0,file)     # Insert that file path inside box
    
    # it lets the user select existing ".pak" file
    # and shows that file path in the input box
    def browse_packed():
        
        file = filedialog.askopenfilename(filetypes=[
            ("Packed Files", "*.pak"),  # shows file with .pak extension
            ("All Files", "*.*")])      # shows all files
        
        packed_entry.delete(0, tk.END)  # Delete old input clear the field
        packed_entry.insert(0, file)    # and insert that in the box
        
        # Example : /home/shubham/Desktop/backup.pak

    def start_packing():
        
        # gets intput from box
        folder = folder_entry.get()     # folder = "/home/shubham/files"
        output = output_entry.get()     # output = "/home/shubham/backup.pak"
        
        print(output)
        # check if user selected folder and file 
        if not folder or not output:
            messagebox.showerror("Error","Please select folder and output file")
            return
        
        # checks if folder is a directory or not
        if not os.path.isdir(folder):
            messagebox.showerror("Error","Invalid Folder selected")
            return
        
        # update status label
        status_label.config(text="packing in progress...")
        
        # Update GUI Immedietely
        root.update_idletasks()
        
        try:
            # stored files from the folder
            files = os.listdir(folder)
            
            total = len(files) # count the files
            
            # Fake Progress Loop
            for i in range(len(files)):
                progress["value"] = (i+1) / total * 100
                root.update_idletasks() # update progress bar visually
            
            pack_folder(folder,output) # call actual packing function
            
            progress["value"] = 100  # Ensure the bar is full
            
            status_label.config(text = "Packing Completed Successfully")  # Show success 
            messagebox.showinfo("Success", "Packing Completed!")        # shows pop up message 
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
            status_label.config(text="Error Occurred")

    def Start_unpacking():
        
        # fetch the packed file path
        packed = packed_entry.get()
        
        if not packed:
            messagebox.showerror("Error","Please select packed file")
            return
        
        # check if it is a file or not 
        if not os.path.isfile(packed):
            messagebox.showerror("Error", "Please Select Valid Packed File")
            return        

        # update label status 
        status_label.config(text="Unpacking in progress")
        
        # REfresh the GUI 
        root.update_idletasks()
        
        try :
            # set fake progress to 30 
            progress["value"] = 30
            
            # shows progress bar movement
            root.update_idletasks()
            
            # Call unpack function
            Unpack_file(packed)
            
            # set progress value to 100
            progress["value"] = 100
            
            # Update the label
            status_label.config(text="Unpacking Completed Successfully!")
            
            # Set pop up message
            messagebox.showinfo("Success", "Unpacking completed!")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))
            status_label.config(text="Error Occurred!")

    # ---------------------------- GUI --------------------------------------

    # Main Window of our app 
    root = tk.Tk()
    
    # Set the title of the app
    root.title("File Packer & Unpacker")
    
    # Set The dimension
    root.geometry("500x550")
    root.resizable(False,False)

    # set the label and sets the font and sie of the font and style
    tk.Label(root,text="File Packer & Unpacker",font=("Arial",16,"bold")).pack(padx=10) # places label with horizontal padding

    #------------------ PACK SECTION -----------------

    tk.Label(root,text="Select Folder").pack()  # text label pack() is like add()
    
    folder_entry = tk.Entry(root,width=50) # Input box for folder path
    folder_entry.pack(pady=5)

    # Button For Browse Folder 
    tk.Button(root,text="Browse Folder",command=browse_folder).pack() # command is the function to run when we click the button

    # Label for output
    tk.Label(root,text="Ouput Packed File").pack(pady=5)
    
    # Input Box for .pak file path
    output_entry = tk.Entry(root,width=50)
    output_entry.pack(pady=5)

    # Button For Save As 
    tk.Button(root, text="Save As",command=browse_output).pack()

    # Button For Start Packing 
    tk.Button(root,text="Start Packing",bg="lightgreen",command=start_packing).pack(pady=10)

    #--------------------- UNPACK SECTION --------------------

    # Label for Packed File]
    tk.Label(root,text="Select Packed File").pack()
    
    # Input Box for .pak file
    packed_entry = tk.Entry(root,width=50)
    packed_entry.pack(pady=5)

    # Button for Browse packed file 
    tk.Button(root,text="Browse Packed File",command=browse_packed).pack()
    
    # Button for start Unpacking
    tk.Button(root,text="Start Unpacking",bg="lightblue",command=Start_unpacking).pack(pady=10)

    #-------------------- PROGRESS BAR -------------------

    # Progress bar
    progress = ttk.Progressbar(root,orient="horizontal",length=400,mode="determinate")
    progress.pack(pady=15)

    #---------------------- STATUS --------------------------

    # Satus label for app 
    status_label = tk.Label(root,text="Status: Ready",fg="blue")
    status_label.pack()

    # For keeping window running waits for using actions 
    root.mainloop()
            
def main():
    
    Create_gui()

if __name__ == "__main__":
    main()