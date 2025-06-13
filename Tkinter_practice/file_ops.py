import tkinter as tk # importing libraries
from tkinter import filedialog


def open_file():# defining a funtion open file
    filepath = filedialog.askopenfilename( # using the function named filedialog.askopenilename from the tkinter module to open a dialog box.
        title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")) # the .txt files will be recommended at starting
    )
    if filepath: # if file is chosen and opened the .txt file
        with open(filepath, "r") as file: # opens the chosen file
            content = file.read() # reading the file
            text_box.delete("1.0", tk.END) # I CANT UNDERSTAND THIS LINE BUT IT IS DELETING SOMETHING
            text_box.insert(tk.END, content) # it inserts the text data from the file to the window

def save_file(): # function to save the file
    filepath = filedialog.asksaveasfilename( # opening a dialog box window
        defaultextension=".txt", # setting the extension as txt
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
    )
    if filepath: # if the file is not empty create a file or open the file in write mode
        with open(filepath, "w") as file:
            content = text_box.get("1.0", tk.END) # get the file name
            file.write(content.strip()) # writes the content to the file


root = tk.Tk() # accessing class TK
root.title("File Example") # naming the window title
root.geometry("400x250") # aspect ratio of the window

# Button frame
button_frame = tk.Frame(root) # creates a button frame
button_frame.pack(pady=10) # adds the padding around the element in button_frame

open_btn = tk.Button(button_frame, text="Open", command=open_file)# creating a button, if it is pressed, the open_file function will be called
open_btn.pack(side="left", padx=10)

save_btn = tk.Button(button_frame, text="Save", command=save_file) # if the button is pressed, the save_file function should be called
save_btn.pack(side="right", padx=10)

# Limited-height Text box
text_box = tk.Text(root, height=10, wrap="word")  # Only 10 lines
text_box.pack(padx=10, pady=10, fill="x")  # Fill only horizontally

root.mainloop()
