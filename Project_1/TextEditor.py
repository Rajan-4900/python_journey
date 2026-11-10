# import tkinter for creating GUI apps
import tkinter as tk

from tkinter import filedialog, messagebox      

# Basic Structure of Main Window
root = tk.Tk()
root.title("Zoro Text Editor")      # Title Of the Text Editor Name
root.geometry("800x600")            # Size od the editor


# Create a text area
text = tk.Text(
    root,                           # Parent Windo
    wrap=tk.WORD,                   # wrap text by word (not by single charector) in next line
    font = ("Helvetica", 12)        # Font style and size
)

text.pack(expand=True, fill=tk.BOTH)

# Main logic start now

# Function 1 --> To create a new file
def new_file():
    text.delete(1.0, tk.END)        # it will open new file with no text like new empty notes

# Function 2---> open a new file
def open_file():
    # Open file dialogue
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes = [("Text files", "*.txt")]
    )

    if file_path:
        # open selected file
        with open(file_path,"r") as file:
            # clear exisitng text 
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# Finction 3 --> Saving the file
def save_file():
    # open save file dialogue
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes = [("Text file", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved succesfully")

# Menu Bar
menuBar = tk.Menu(root)
root.config(menu = menuBar)
file_menu = tk.Menu(menuBar)

# new file, open file, save file, exit file

# Add file menu to menu bar
menuBar.add_cascade(label="File", menu=file_menu)

# File menu inside the options List
file_menu.add_command(label="New File", command=new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)



# starts and eeps the window open
root.mainloop()   