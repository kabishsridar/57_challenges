room_length = int(input("What is the length of the room in feet? ")) # prompt user for length of room
room_width = int(input("What is the width of the room in feet? ")) # prompt user for width of room
print(f"You entered dimensions of {room_length} feet by {room_width} feet.") # display dimensions
area_in_feet = room_width * room_length # calculate area of room
area_in_metre_sq = area_in_feet * 0.09290304 # convert to square meters
print(f"The area is \n{area_in_feet} square feets \n{area_in_metre_sq} square meters") # display the final output