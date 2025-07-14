fin = open('typing_23.txt', 'r')
data = fin.read()
words = data.split()
count = len(words)
print(f"The total number of the words: {count}")
duration = 10
wpm = count // duration
print(f"The words per minute: {wpm}")
fin.close()