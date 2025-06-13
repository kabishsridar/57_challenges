import tkinter as tk  # standard alias
def say_hello():
    print("Hello!")
def text_to_window():
    label = tk.Label(root, text="Hello")
    label.pack()
root = tk.Tk()  # Create the main window
root.title("My First Tkinter App")  # Window title
root.geometry("300x200")  # Width x Height
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()
button1 = tk.Button(root, text="click Me", command=text_to_window)
button1.pack()
# button1.grid(row=5, column=0) # grid and pack cannot be used in the same script
entry = tk.Entry(root)
entry.pack()
text = tk.Text(root, height=5, width=30)
text.pack()
root.mainloop()