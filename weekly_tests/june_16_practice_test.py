# one shirt increment for each event
# the second line of input is which lan gets shirt on that day
lst = []

""" for inp in range(2):
    prompt = input("").split()
    lst.append(prompt)
# print(lst) """
with open('june_16_text.txt', 'r') as fin: # opening a file in read mode as an input
    data = fin.readlines() # read each line in the file and store it to data
    
clean = int(lst[0][0])
total = int(lst[0][0])
events = int(lst[0][1])
days = int(lst[0][2])
event_days = []
for day in lst[1]:
    event_days.append(int(day))

laundry = 0
# print(f"n :{clean} E :{events} D: {days}")
for day in range(1, days+1):
    if clean ==0:
        laundry +=1
        clean = total
    clean -=1

    if day in event_days:
        clean += 1
        # print(day)
    
print(laundry)