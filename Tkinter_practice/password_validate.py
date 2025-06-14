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
""" for row in rows:
    print(row) """

root = tk.Tk() # using Tk class and storing it
root.title('get input') # window title
root.geometry("300x200") # size of the window

tk.Label(root, text="Username").grid(row=0, column=0)
name = tk.Entry(root) # ask for user name
name.grid(row=0, column=1)

tk.Label(root, text="Password").grid(row=1, column=0)
passwd = tk.Entry(root, show='*') # ask for password
passwd.grid(row=1, column=1)

def submit(): # function to submit the records to mysql
    cur.execute('SELECT * FROM PASSWORD;')
    rows = cur.fetchall() # gets all the data from mysql table
    input_name = name.get()
    input_passwd = passwd.get()
    if input_name not in rows[0]: # if user not already exists insert the user name and password
        cur.execute("INSERT INTO PASSWORD VALUES (%s, %s);", (input_name, input_passwd))
        mycon.commit()
        print("Saved")
    else:
        print("User already exists") # if already exists, display user already exists
    # check user already in the database
    # if not insert to database
    # else, inform the customer


def validate_python(): # validating password
    cur.execute('SELECT * FROM PASSWORD;')
    rows = cur.fetchall() # gets all the data from mysql 
    input_name = name.get()
    input_passwd = passwd.get()
    
    my_dict = {} # initiating my_dict to an empty dictionary
    # my_dict.update({"kabish": "12345"})
    # print(my_dict)

    status = False # initiating status to track whether the password is correct or something else
    for row in rows:
        my_dict.update({f"{row[0]}" : f"{row[1]}"}) # getting the data from mysql and adding to the dictionary
    # print(my_dict)
    if input_name not in my_dict: # if the user name is not in the dictionary
        print("User not registered") # display user not registered
    else: # if already exists
        for key, value in my_dict.items():
            if key == input_name and value == input_passwd: # check whether the entered name and password matches
                status = True # then true
        if status == True:
            print("Correct Password")
        
        else: # if the name and password doesn't matches
            print("Wrong password")
    
def validate_sql(): # validating through sql
    cur.execute('SELECT * FROM PASSWORD;')
    rows = cur.fetchall()
    input_name = name.get()
    input_passwd = passwd.get()
    cur.execute(f"SELECT * FROM PASSWORD WHERE USERNAME = '{input_name}' AND PASSWORD = '{input_passwd}';") # displays the output if name and password matches
    output = cur.fetchall()
    if output: # if the output is not empty
        print("CORRECT PASSWORD")
        print(f'{output} is available In MYSQL')
    else: # if the output is emty set, then there are no matches in the dictionary
        print("Wrong password")
    # if user in db
    # then  check password
    # if password matches, print correct password
    # else, print wrong password

button = tk.Button(root, text="validate python", command=validate_python) # button to validate through python
button.grid(row=3, column=0)
button = tk.Button(root, text="validate", command=validate_sql) # button to validate through sql
button.grid(row=2, column=3)
button = ttk.Button(root, text="Submit", command=submit) # button to save the data to sql
button.grid(row=2, column=0)

root.mainloop()