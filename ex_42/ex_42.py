fin = open("C:\\kabish_python\\57_challenges\\ex_42\\without_aligned.csv", 'r') # open a csv file
names = [] # initiate an empty list named names to store the name in csv file
lines = fin.readlines() # read every lines and store as lines

for line in lines: # loop through each line
    stripped_line = line.strip()
    if stripped_line:
        names.append(f"{stripped_line}") # append the line to names

print(f"{'Last':<10} | {'First':<12} | {'Salary':<10}") # aligning headings
print("-"* 40)

for line in lines: # loop through each line 
    stripped_line = line.strip()
    if stripped_line:  # Ignore empty lines
        parts = stripped_line.split(',') # wherever the comma is detectd, seperate there
        if len(parts) == 3:
            last, first, salary = parts
            print(f"{last:<10} | {first:<12} | {salary:<10}") # display output

fin.close() # close the files