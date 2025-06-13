import tkinter as tk # importing the required modules
from tkinter import filedialog
from PIL import Image, ImageTk


def open_image(): # creating a function named open_image
    filepath = filedialog.askopenfilename( # opens the dialog box
        title="Open Image", # displayed for the window title
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")], # opens only those mentioned file extensions
    )
    if filepath:
        global img  # Keep a reference to avoid garbage collection
        image = Image.open(filepath) # opens the file
        img = ImageTk.PhotoImage(image.resize((300, 300)))  # Resize for display
        image_label.config(image=img) # configuring size


def save_image(): # create function to save image
    filepath = filedialog.asksaveasfilename( # opens a dialog box
        defaultextension=".png", # set default extension to png
        filetypes=[
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpg"),
            ("All Files", "*.*"),
        ],
    )
    if filepath: # if the file is found
        image = img._PhotoImage__photo  # Get the original Tk image reference
        # Re-save from original Pillow object instead of Tk image:
        original = Image.open(filedialog.askopenfilename())  # Reopen to save
        original.save(filepath) # save the image to the file path


root = tk.Tk() # using class Tk
root.title("Image Viewer") # window title
root.geometry("400x400") # the size or aspect ration of dialog box

tk.Button(root, text="Open Image", command=open_image).pack(pady=10) # button to open image
tk.Button(root, text="Save Image", command=save_image).pack(pady=10) # button to save image

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()
