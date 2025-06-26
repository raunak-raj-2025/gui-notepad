##Importing useful things:
import tkinter as tk
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename as aof, asksaveasfilename as asf
import os

##Creating a window:
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("720x1540")

## Creating commands of menubar:

#Creating commands of file menu:
def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    text_area.delete(1.0, "end")
    
def Open():
    global file
    file = aof(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    if file == "":
        file = None
        
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text_area.delete(1.0, "end")
        with open(file, "r") as f:
            text_area.insert(1.0, f.read())
    
def Save():
    global file
    if file == None:
        file = asf(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        
        if file == "":
            file = None
            
        else:
            with open(file, "w") as f:
                f.write(text_area.get(1.0, "end"))
            root.title(os.path.basename(file) + " - Notepad")
            
    else:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, "end"))
    
def exit():
    root.destroy()
    
#Creating commands of edit menu:
def cut():
    text_area.event_generate(("<<cut>>"))
    
def copy():
    text_area.event_generate(("<<cut>>"))
    
def paste():
    text_area.event_generate(("<<cut>>"))
    
#Creating commands of help menu:
def about():
    tmsg.showinfo("About us", "This is Raunak's Notepad")

##Creating a label which shows write here:
tk.Label(root, text="Write Here!", font="comicsansms 20 bold", bg="grey").pack(fill="x")

##Creating text area:
text_area = tk.Text(root, font="lucida 10", bg="grey")
text_area.pack(expand=True, fill="both")
file = None

##Creating scrollbar:
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)

##Creating menubar:
menubar = tk.Menu(root)
root.config(menu=menubar)

#Creating cascade of file menu:
file_menu = tk.Menu(menubar)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=Open)
file_menu.add_command(label="Save", command=Save)
file_menu.add_separator()
file_menu.add_command(label="exit", command=exit)

menubar.add_cascade(label="File", menu=file_menu)

#Creating cascade of edit menu:
edit_menu = tk.Menu(menubar)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

menubar.add_cascade(label="Edit", menu=edit_menu)

#Creating cascade of help menu:
help_menu = tk.Menu(menubar)
help_menu.add_command(label="About", command=about)

menubar.add_cascade(label="Help", menu=help_menu)

##Running the window:
root.mainloop()