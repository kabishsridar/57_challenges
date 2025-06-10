print("Take a number dispenser mahine: ")
take_counts = [] # inititating take_counts as an empty list
def late_students(take_counts): # function to count the number of late students
    late_students_count = 0
    for line in lines: # loop through each lines in the file
        if line == "TAKE\n": # if it is take, then increment 1 to the late_students_count
            late_students_count += 1
        elif line == "CLOSE\n": # if it is close, then it should append the counts to take_counts for every close
            take_counts.append(late_students_count)
            late_students_count = 0 # reset the count for the every CLOSE
    #for count in take_counts:
    #    print(count)
results = [] # initiating results as an empty list
def remaining_students(results): # function to count the number of remaining students
    count_take = 0
    count_serve = 0
    
    for line in lines: # loop through each line in the file
        if line == "TAKE\n":
            count_take += 1
        elif line == "SERVE\n":
            count_serve += 1
        elif line == "CLOSE\n": # counts the number of takes and serves, then subtracts serves from the takes to fincd the remaining
            results.append(count_take - count_serve) # appending them to count_take and resets
            count_take = 0 # resets after every close
            count_serve = 0
    #for count in results:
    #    print(count)
# print(type(lines[0]))
next_numbers = [] # initiating the next_numbers as an empty list
def next_num(next_numbers): # function to find the next numbers
    
    initial_num = int(lines[0]) # converting the first line of the file to integer, which is the initial next number
    for line in lines: # loop through each lines in the file
        if line == "TAKE\n":
            initial_num += 1 # increment 1 every time when the line is take, so that we can find the next number
        elif line == "CLOSE\n":
            next_numbers.append(initial_num) # appending next numbers before close for every close
    #for count in next_numbers:
    #    print(count)

def ordering(take_counts, results, next_numbers): # function to reorder the output as per the sample output given in the question.
    for i in range(len(take_counts)):
        print(take_counts[i], results[i], next_numbers[i])
        
if __name__ == "__main__":
    fin = open('attendence.txt', 'r') # opening the file in read mode
    lines = fin.readlines() # reading all the lines in the file and storing them in a list
    late_students(take_counts) # calling the function
    remaining_students(results) # calling the function
    next_num(next_numbers) # calling the function
    ordering(take_counts, results, next_numbers)
    fin.close() # closing the file