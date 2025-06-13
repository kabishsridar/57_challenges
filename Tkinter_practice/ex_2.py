import tkinter as tk

def on_key(event):
    print(f"You pressed {event.char}")
root = tk.Tk()
entry = tk.Entry(root)
entry.bind("<Key>", on_key)  # Binds to all key presses
entry.pack()
root.mainloop()