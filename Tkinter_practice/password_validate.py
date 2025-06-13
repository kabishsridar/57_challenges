import tkinter as tk # importing modules
from tkinter import ttk
import mysql.connector as sqltor

# connecting to mysql
mycon = sqltor.connect(host='localhost', user='root', passwd='2007kabish', database='tkinter')
if mycon.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")
cur = mycon.cursor() # setting up a cursor instance

cur.execute('SELECT * FROM PASSWORD;') # execute the command in mysql
rows = cur.fetchall() # fetch the executed data from mysql
for row in rows:
    print(row)

root = tk.Tk() # using Tk class and storing it
root.title('get input') # window title
root.geometry("300x200") # size of the window

name_var = tk.StringVar()
tk.Label(root, text="Username").grid(row=0, column=0)
name = tk.Entry(root)
name.grid(row=0, column=1)

passwd_var = tk.StringVar()
tk.Label(root, text="Password").grid(row=1, column=0)
passwd = tk.Entry(root, show='*')
passwd.grid(row=1, column=1)
def submit():
    input_name = name_var.get()
    input_passwd = passwd_var.get()
    # cur.execute("INSERT INTO PASSWORD VALUES (%s, %s);", (input_name, input_passwd))
    # mycon.commit()
    # print("Saved")

def validate(rows):
    input_name = name_var.get()
    input_passwd = passwd_var.get()
    for row in rows:
        print(input_name, input_passwd)
        if row[0] == input_name and row[1] == input_passwd:
            print("CORRECT PASSWORD")
        else:
            print("Wrong match")
validate(rows)
button = ttk.Button(root, text="Submit", command=submit)
button.grid(row=2, column=0)

root.mainloop()