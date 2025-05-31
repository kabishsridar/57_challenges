fin = open('word_frequency.txt','r') # open the file in read mode
content = fin.read() # read the content in file
badger = content.count('badger') # count the number of badgers
mushroom = content.count('mushroom')
snake = content.count('snake')
print(f"badger:   {badger * '*'}") # display * for number of badgers
print(f"mushroom: {mushroom * '*'}") # display * for number of mushrooms
print(f"snake:    {snake * '*'}") # display * for number of snake