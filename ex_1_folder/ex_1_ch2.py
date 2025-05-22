# print(f"Hello, {name}, nice to meet you !" if (name:= input("What is your name? ")) == "kabish" else "hi how are you")
name = input("What is your name? ")
if name.lower == "kabish":
    print(f"Hello {name}, nice to meet you")
elif name.lower == "kamal":
    print(f"hey {name} how are you")
else :
    print(f"hi {name} whatsup")