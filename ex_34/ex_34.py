# assign employees name to a list named employees
employees = ["john smith", "jackie jackson", "chris jones", "amanda cullen", "jeremy godwin"]
print(f"There are {len(employees)} employees:") # display number of employees in list
for employee in employees:
    print(employee) # display all employees name
remove = input("\nEnter an employee name to remove: ") # prompt the user for name to be removed
def remove_employee():
    for employee in employees: # loop for each employees
        if remove == employee: # if the input by the user matches with any employee name remove the name
            employees.remove(remove)
    print(f"\nThere are {len(employees)} employees.") # display number of employees after removing
    for unchanged in employees: # display the employee names except the removed one
        print(unchanged)

if __name__ == "__main__":
    remove_employee()