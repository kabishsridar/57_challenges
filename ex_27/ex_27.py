def employee_id(inp):
    if len(inp) != 6:
        print("not valid. the Employee Id contains 6 characters")
    if not inp[0].isalpha() or not inp[1].isalpha():
        print("not valid, the first two characters should be Alphabets")
    if inp[2] != "-":
        print("not valid, after two numbers, hyphen should be there")
    if not (inp[3:].isdigit() and inp[4].isdigit() and inp[5].isdigit()):
        print("not valid, last four characters should be integers")
    else:
        print("Correct EID")
def firstname(fname):
    if fname == "":
        print("The first name cannot be empty")
    if len(fname) <= 2:
        print("First name cannot be less than 2 letters")
    else:
        print("Correct first name")
def lastname(lname):
    if lname == "":
        print("The last name can not be empty")
    if len(lname) <= 2:
        print("The last name can not be less than 2 letters")
    else:
        print("Correct last name")

def zip_code(zip):
    if not zip.isdigit():
        print("The zip code must be integer")
    else:
        print("Correct zip code")
def validate_input(fname, lname, eid, zip):
    firstname(fname)
    lastname(lname)
    employee_id(eid)
    zip_code(zip_c)

# Input section
fname = input("Enter the first name: ")
lname = input("Enter the last name: ")
zip_c = input("Enter the zip code: ")
emp_id = input("Enter the employee ID: ")

validate_input(fname, lname, emp_id, zip_c)
