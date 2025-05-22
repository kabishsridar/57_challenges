unit = "" # initiating unit as an empty string
def choose_unit(): # defining a function to choose the units by the user
    global unit
    units = input("Choose between Feet or Meters to display the output: ") # prompt the user for unit
    if units in ["meter", "meters", "square meter", "square meters"]: # check whether it is meters, if it is meters, then the unit will be square meters
        unit = "Square meters"
    elif units in ["feet","feets","Square feet","Square feets"]: # else it is square feet
        unit = "Square feet"
def isinteger(a): # checking whether it is a digit
    if a.isdigit(): 
        return True
    else:
        print("Only integers accepted") # if it is not a digit, it should print only integers accepted
        return False

room_length = (input("What is the length of the room in feet? ")) # prompt user for length of room
room_width = (input("What is the width of the room in feet? ")) # prompt user for width of room
print(f"You entered dimensions of {room_length} feet by {room_width} feet.") # display dimensions

length = int(room_length) # converting into integer to make arithmetic operations
width = int(room_width)

area_in_feet = width * length # calculate area of room
area_in_metre_sq = area_in_feet * 0.09290304 # convert to square meters


if isinteger(room_length) and isinteger(room_width) : # it should run only if it is a digit 
    choose_unit()
    print(f"The area is {area_in_feet} square feets" if unit == "Square feet" else f"{area_in_metre_sq} square meters")