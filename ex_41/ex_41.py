f = open('alphabetising.txt', 'r') # open file in read mode
names = []  # initialize an empty list to store names
for line in f:
    stripped_line = line.strip()
    if stripped_line:
        names.append(stripped_line)
f.close()

def sort(names): # Function to sort names alphabetically
    sorted_names = []  # Create a new list for sorted names
    sorted_names = sorted(names)
    return sorted_names

def write(filename, sorted_names): # Function to write sorted names to a new file
    fout = open(filename, 'w')
    fout.write(f"Total of {len(sorted_names)} names\n")
    fout.write("-" * 30 + "\n")
    for name in sorted_names:
        fout.write(name + "\n")
    fout.close()  # Close the file
sorted_list = sort(names) # Sort and write names to a new file
write('alphabet_sorted.txt', sorted_list)
print("Sorted names have been saved to 'alphabet_sorted.txt'.")