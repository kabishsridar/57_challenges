fin = open('Typing_practice\\typing_01.txt', 'r')
data = fin.read()
words = data.split()
count = len(words)
print(f"The total number of the words: {count}")
duration = 5
wpm = count // duration
print(f"The words per minute: {wpm}")
fin.close()