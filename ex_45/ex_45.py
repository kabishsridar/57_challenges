file = input("Enter the name of output file: ") # prompt for output file name
infile = open('finder.txt','r') # open the file in read mode to read the content to be modified
content = infile.read() # read the file
modified = content.replace("utilize", "use") # replace use in place of utilize
outfile = open(file, 'w') # open the file in write mode
outfile.write(modified) # write the modified content to output file
print(f"Modified content written to {file}") # print written message