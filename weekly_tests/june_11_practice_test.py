inp = input("address: ")
def defanging(inp):
    result = []
    for char in inp:
        if char != ".":
            result.append(char)
        if char == ".":
            char = "[.]"
            result.append(char)

    for char in result:
        print(char, end="")
defanging(inp)