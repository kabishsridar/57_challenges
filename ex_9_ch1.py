def isinteger(a):
    if a.isdigit():
        return True
    else:
        print("Only numbers accepted")
        return False
    
def circle():
    r = (input("Enter the radius of ceiling(sq feet): ")) # prompt for radius
    
    if isinteger(r):
        r = int(r)
        area = 3.14 * r**2
        gallon = 350 # initiating gallon as 350 as one gallon covers 350 sq feet
        num_gallon = (area // gallon ) + 1 # we need 1 complete gallon extra if even for 351 sq feets, two gallons are required
        # displaying the final output
        print(f"You will need to purchase {num_gallon} gallons of paint \nto cover {area} square feet. ")

def rectangle():
    h = (input("Enter the height of ceiling(sq feet): ")) # prompt for width
    l = (input("Enter the radius of ceiling(sq feet): ")) # prompt for length
    
    if isinteger(h) and isinteger(l):
        h = int(h)
        l = int(l)
        gallon = 350 # initiating gallon as 350 as one gallon covers 350 sq feet
        area = h * l
        num_gallon = (area // gallon ) + 1 # we need 1 complete gallon extra if even for 351 sq feets, two gallons are required
        # displaying the final output
        print(f"You will need to purchase {num_gallon} gallons of paint \nto cover {area} square feet. ")
def Lshaped():
    print("For L-shaped room, kindly seperate those as two rectangles")
    h1 = (input("Enter the height of ceiling 1 (sq feet): ")) # prompt for width
    l1 = (input("Enter the radius of ceiling 1 (sq feet): ")) # prompt for length
    h2 = (input("Enter the height of ceiling 2 (sq feet): ")) # prompt for width
    l2 = (input("Enter the radius of ceiling 2 (sq feet): ")) # prompt for length
    
    if isinteger(h1) and isinteger(h2) and isinteger(l1) and isinteger(l2):
        h1 = int(h1)
        h2 = int(h2)
        l1 = int(l1)
        l2 = int(l2)
        area1 = h1 * l1
        area2 = h2 * l2
        total_area = area1 + area2
        gallon = 350 # initiating gallon as 350 as one gallon covers 350 sq feet
        num_gallon = (total_area // gallon ) + 1 # we need 1 complete gallon extra if even for 351 sq feets, two gallons are required
        # displaying the final output
        print(f"You will need to purchase {num_gallon} gallons of paint \nto cover {total_area} square feet. ")

def choose_room():
    room = input("Enter the room(L-shaped, round, rectangle): ")
    if room.lower() == "round":
        circle()
    elif room.lower() == "rectangle":
        rectangle()
    if room.lower() in ["l-shaped", "lshaped", "l shaped"]:
        Lshaped()
       
choose_room()