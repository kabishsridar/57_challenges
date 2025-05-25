def isanagram(word1, word2):
    # length should be same
    # all the letters can be misarranged but should present
    if len(word1) == len(word2):
        return True
    return sorted(word1.lower()) == sorted(word2.lower())

print("Enter two strings and I'll tell you if they \nare anagrams: ")
word1 = input("Enter the first string: ").strip()
word2 = input("Enter the second string: ").strip()

if isanagram(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print("These are not anagrams")