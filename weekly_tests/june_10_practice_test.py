# print("Take a number dispenser mahine: ")
fin = open('attendence.txt', 'r')
lines = fin.readlines()
take_counts = []
def late_students(take_counts):
    late_students_count = 0
    for line in lines:
        if line == "TAKE\n":
            late_students_count += 1
        elif line == "CLOSE\n":
            take_counts.append(late_students_count)
            late_students_count = 0
    #for count in take_counts:
    #    print(count)
late_students(take_counts)
results = []
def remaining_students(results):
    count_take = 0
    count_serve = 0
    
    for line in lines:
        if line == "TAKE\n":
            count_take += 1
        elif line == "SERVE\n":
            count_serve += 1
        elif line == "CLOSE\n":
            results.append(count_take - count_serve)
            count_take = 0
            count_serve = 0
    #for count in results:
    #    print(count)
remaining_students(results)

# print(type(lines[0]))
next_numbers = []
def next_num(next_numbers):
    
    initial_num = int(lines[0])
    for line in lines:
        if line == "TAKE\n":
            initial_num += 1
        elif line == "CLOSE\n":
            next_numbers.append(initial_num)
    #for count in next_numbers:
    #    print(count)
next_num(next_numbers)

def ordering(take_counts, results, next_numbers):
    for i in range(len(take_counts)):
        print(take_counts[i], results[i], next_numbers[i])
ordering(take_counts, results, next_numbers)
fin.close()