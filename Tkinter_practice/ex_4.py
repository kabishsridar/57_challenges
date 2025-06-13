import tkinter as tk
root = tk.Tk()
root.geometry("200x300")
form_frame = tk.Frame(root)
form_frame.pack(padx=10, pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0)
name = tk.Entry(form_frame)
name.grid(row=0, column=1)

tk.Label(form_frame, text="password:").grid(row=1, column=0)
passwd = tk.Entry(form_frame)
passwd.grid(row=1, column=1)

# entry = tk.Entry(root)
# entry.pack()

def show_value():
    input_name= name.get()  # Get input text
    input_password = passwd.get()
    label_text = f"hi {input_name}, and your password is {input_password}"
    tk.Label(form_frame, text=label_text).grid(row=4, column=0)
tk.Button(root, text="Print", command=show_value).pack()
root.mainloop()